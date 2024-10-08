# 3.py 
# 62. 類似度の高い単語10件
# “United States”とコサイン類似度が高い10語と，その類似度を出力せよ．
import gensim
import logging
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

def main() -> None:
    model_path = "data/GoogleNews-vectors-negative300.bin"
    target_word = "United_States"

    manager = WordVectorManager(model_path)

    try:
        manager.load_model()
        similar_words: List[Tuple[str, float]] = manager.get_most_similar(target_word)
        
        print(f"'{target_word}'とコサイン類似度が高い10語とその類似度:")
        for word, similarity in similar_words:
            print(f"{word}: {similarity:.4f}")
    except FileNotFoundError as e:
        logging.error(f"ファイルが見つかりません: {e}")
    except ValueError as e:
        logging.error(f"モデルの読み込みエラー: {e}")
    except Exception as e:
        logging.error(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()