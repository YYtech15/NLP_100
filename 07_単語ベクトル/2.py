# 2.py 
# 61. 単語の類似度
# “United States”と”U.S.”のコサイン類似度を計算せよ．
import logging
from typing import Optional
import seven_lib

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main() -> None:
    model_path = "data/GoogleNews-vectors-negative300.bin"
    word1 = "United_States"
    word2 = "U.S."

    manager = seven_lib.WordVectorManager(model_path)

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