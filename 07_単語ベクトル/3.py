# 3.py 
# 62. 類似度の高い単語10件
# “United States”とコサイン類似度が高い10語と，その類似度を出力せよ．
import logging
import seven_lib
from typing import List, Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main() -> None:
    model_path = "data/GoogleNews-vectors-negative300.bin"
    target_word = "United_States"

    manager = seven_lib.WordVectorManager(model_path)

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