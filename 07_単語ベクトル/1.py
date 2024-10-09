# 1.py
# 60. 単語ベクトルの読み込みと表示
# Google Newsデータセット（約1,000億単語）での学習済み単語ベクトル（300万単語・フレーズ，300次元）
# をダウンロードし，”United States”の単語ベクトルを表示せよ．
# ただし，”United States”は内部的には”United_States”と表現されていることに注意せよ．
import logging
import seven_lib

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_vector(word: str, vector) -> None:
    if vector is not None:
        print(f"'{word}' の単語ベクトル:")
        print(vector)
    else:
        print(f"'{word}' の単語ベクトルを表示できません")

def main():
    compressed_path = "data/GoogleNews-vectors-negative300.bin.gz"
    decompressed_path = "data/GoogleNews-vectors-negative300.bin"
    target_word = "United_States"

    manager = seven_lib.WordVectorManager(compressed_path, decompressed_path)

    try:
        manager.prepare_file()
        manager.load_model()
        vector = manager.get_word_vector(target_word)
        display_vector(target_word, vector)
    except FileNotFoundError as e:
        logging.error(f"ファイルが見つかりません: {e}")
    except ValueError as e:
        logging.error(f"モデルの読み込みエラー: {e}")
    except Exception as e:
        logging.error(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
