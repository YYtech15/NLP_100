import gensim
import logging
import gzip
import shutil
import numpy as np
from pathlib import Path
from typing import List, Optional, Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WordVectorManager:
    def __init__(self, compressed_path: str, decompressed_path: str) -> None:
        self.compressed_path: Path = Path(compressed_path)
        self.decompressed_path: Path = Path(decompressed_path)
        self.model: Optional[gensim.models.KeyedVectors] = None

    def prepare_file(self) -> None:
        if self.decompressed_path.exists():
            logging.info(f"解凍済みファイルを使用します: {self.decompressed_path}")
            return

        if not self.compressed_path.exists():
            raise FileNotFoundError(f"圧縮ファイルが見つかりません: {self.compressed_path}")

        logging.info(f"圧縮ファイルを解凍します: {self.compressed_path} -> {self.decompressed_path}")
        with gzip.open(self.compressed_path, 'rb') as f_in:
            with open(self.decompressed_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        logging.info("ファイルの解凍が完了しました")

    def load_model(self) -> None:
        '''
        Load the word vector model.
        
        Raises:
            FileNotFoundError: If the model file is not found.
        '''
        if not self.decompressed_path.exists():
            raise FileNotFoundError(f"モデルファイルが見つかりません: {self.decompressed_path}")

        logging.info(f"モデルを読み込んでいます: {self.decompressed_path}")
        # gensimのKeyedVectorsを使用してバイナリ形式のモデルを読み込む
        self.model = gensim.models.KeyedVectors.load_word2vec_format(str(self.decompressed_path), binary=True)
        logging.info("モデルの読み込みが完了しました")

    def get_word_vector(self, word: str) -> Optional[np.ndarray]:
        if self.model is None:
            raise ValueError("モデルが読み込まれていません")

        try:
            return self.model[word]
        except KeyError:
            logging.warning(f"単語 '{word}' はモデル内に存在しません")
            return None
    
    def cos_similarity(self, word1: str, word2: str) -> Optional[float]:
        '''
        Calculate the cosine similarity between two words.
        
        Args:
            word1 (str): The first word.
            word2 (str): The second word.
        
        Returns:
            Optional[float]: The cosine similarity between the two words, or None if the words are not found.
        '''
        vector1 = self.get_word_vector(word1)
        vector2 = self.get_word_vector(word2)

        if vector1 is None or vector2 is None:
            return None

        return float(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
    
    def get_most_similar(self, word: str, topn: int = 10) -> List[Tuple[str, float]]:
        '''
        Get the most similar words to the given word.
        
        Args:
            word (str): The word to find similar words for.
            topn (int): The number of similar words to return.
        
        Returns:
            List[Tuple[str, float]]: A list of tuples containing similar words and their cosine similarities.
        '''
        if self.model is None:
            raise ValueError("モデルが読み込まれていません")

        try:
            return self.model.most_similar(word, topn=topn)
        except KeyError:
            logging.warning(f"単語 '{word}' はモデル内に存在しません")
            return []
    
    def perform_analogy(self, pos1: str, neg1: str, pos2: str) -> Optional[np.ndarray]:
        '''
        Perform the analogy operation pos1 - neg1 + pos2.
        
        Args:
            pos1 (str): The first positive word.
            neg1 (str): The negative word.
            pos2 (str): The second positive word.
        
        Returns:
            Optional[np.ndarray]: The resulting vector, or None if any of the input words are not found.
        '''
        vec1 = self.get_word_vector(pos1)
        vec2 = self.get_word_vector(neg1)
        vec3 = self.get_word_vector(pos2)

        if vec1 is None or vec2 is None or vec3 is None:
            return None

        return vec1 - vec2 + vec3
    
    def analogy(self, word1: str, word2: str, word3: str) -> Tuple[Optional[str], Optional[float]]:
        vec1 = self.get_word_vector(word1)
        vec2 = self.get_word_vector(word2)
        vec3 = self.get_word_vector(word3)

        if vec1 is None or vec2 is None or vec3 is None:
            return None, None

        result_vector = vec2 - vec1 + vec3
        most_similar = self.get_most_similar(result_vector)
        
        if most_similar:
            return most_similar[0]
        else:
            return None, None
    
    def get_most_similar_to_vector(self, vector: np.ndarray, topn: int = 10) -> List[Tuple[str, float]]:
        if self.model is None:
            raise ValueError("モデルが読み込まれていません")

        return self.model.similar_by_vector(vector, topn=topn)