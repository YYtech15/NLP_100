# 1.py
# 60. 単語ベクトルの読み込みと表示Permalink
# Google Newsデータセット（約1,000億単語）での学習済み単語ベクトル（300万単語・フレーズ，300次元）
# をダウンロードし，”United States”の単語ベクトルを表示せよ．
# ただし，”United States”は内部的には”United_States”と表現されていることに注意せよ．
import gensim
import logging
import gzip
import shutil
import numpy as np
from pathlib import Path
from typing import Optional

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

    manager = WordVectorManager(compressed_path, decompressed_path)

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
