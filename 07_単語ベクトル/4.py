# 4.py 
# 63. 加法構成性によるアナロジー
# “Spain”の単語ベクトルから”Madrid”のベクトルを引き，
# ”Athens”のベクトルを足したベクトルを計算し，
# そのベクトルと類似度の高い10語とその類似度を出力せよ
import logging
import seven_lib
from typing import List, Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main() -> None:
    model_path = "data/GoogleNews-vectors-negative300.bin"

    manager = seven_lib.WordVectorManager(model_path)

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
