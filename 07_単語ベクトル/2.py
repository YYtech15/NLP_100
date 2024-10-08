# 2.py 
# 61. 単語の類似度
# “United States”と”U.S.”のコサイン類似度を計算せよ．
import gensim
import logging
import numpy as np
from pathlib import Path
from typing import Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WordVectorManager:
    def __init__(self, model_path: str):
        self.model_path = Path(model_path)
        self.model: Optional[gensim.models.KeyedVectors] = None

    def load_model(self) -> None:
        if not self.model_path.exists():
            raise FileNotFoundError(f"モデルファイルが見つかりません: {self.model_path}")

        logging.info(f"モデルを読み込んでいます: {self.model_path}")
        self.model = gensim.models.KeyedVectors.load_word2vec_format(str(self.model_path), binary=True)
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

def main() -> None:
    model_path = "data/GoogleNews-vectors-negative300.bin"
    word1 = "United_States"
    word2 = "U.S."

    manager = WordVectorManager(model_path)

    try:
        manager.load_model()
        similarity: Optional[float] = manager.cos_similarity(word1, word2)
        if similarity is not None:
            print(f"'{word1}'と'{word2}'のコサイン類似度: {similarity}")
        else:
            print(f"'{word1}'と'{word2}'の類似度を計算できませんでした。")
    except FileNotFoundError as e:
        logging.error(f"ファイルが見つかりません: {e}")
    except ValueError as e:
        logging.error(f"モデルの読み込みエラー: {e}")
    except Exception as e:
        logging.error(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()