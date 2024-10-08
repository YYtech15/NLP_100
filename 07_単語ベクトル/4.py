# 4.py 
# 63. 加法構成性によるアナロジー
# “Spain”の単語ベクトルから”Madrid”のベクトルを引き，
# ”Athens”のベクトルを足したベクトルを計算し，
# そのベクトルと類似度の高い10語とその類似度を出力せよ
import gensim
import logging
import numpy as np
from pathlib import Path
from typing import Optional, List, Tuple

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

    def get_most_similar_to_vector(self, vector: np.ndarray, topn: int = 10) -> List[Tuple[str, float]]:
        if self.model is None:
            raise ValueError("モデルが読み込まれていません")

        return self.model.similar_by_vector(vector, topn=topn)

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

def main() -> None:
    model_path = "data/GoogleNews-vectors-negative300.bin"

    manager = WordVectorManager(model_path)

    try:
        manager.load_model()
        # The resulting vector is meant to represent "If the capital of Spain were replaced by Athens, which country would it belong to?"
        result_vector = manager.perform_analogy("Spain", "Madrid", "Athens")
        if result_vector is not None:
            similar_words: List[Tuple[str, float]] = manager.get_most_similar_to_vector(result_vector)

            print("'Spain - Madrid + Athens' のベクトルに最も類似した10語とその類似度:")
            for word, similarity in similar_words:
                print(f"{word}: {similarity:.4f}")
        else:
            print("ベクトル演算を実行できませんでした。")
    except FileNotFoundError as e:
        logging.error(f"ファイルが見つかりません: {e}")
    except ValueError as e:
        logging.error(f"モデルの読み込みエラー: {e}")
    except Exception as e:
        logging.error(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
