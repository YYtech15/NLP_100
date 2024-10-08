# 5.py 
# 64. アナロジーデータでの実験
# 単語アナロジーの評価データをダウンロードし，
# vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
# そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
# 求めた単語と類似度は，各事例の末尾に追記せよ．
import re
import gensim
import logging
import numpy as np
from pathlib import Path
from typing import List, Tuple, Optional

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

    def get_most_similar(self, vector: np.ndarray, topn: int = 1) -> List[Tuple[str, float]]:
        if self.model is None:
            raise ValueError("モデルが読み込まれていません")

        return self.model.similar_by_vector(vector, topn=topn)

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

def process_analogy_file(file_path: str, manager: WordVectorManager) -> List[str]:
    '''
    Process the analogy file and return the results.
    
    Args:
        file_path (str): The path to the analogy file.
        manager (WordVectorManager): The WordVectorManager instance.
    
    Returns:
        List[str]: A list of lines containing the original analogy and the result word and similarity.
    '''
    results = []
    
    # セクション名のパターン（例: ": capital-common-countries"）
    section_pattern = re.compile(r'^:\s+.*$')
    section_name = ""
    
    # 3つの単語のパターン
    analogy_pattern = re.compile(r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)$')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # セクション名の場合
            if not line:
                results.append(line)
                continue
            
            # セクション名の場合
            if section_pattern.match(line):
                section_name = line.replace(":","").strip()
                continue
            
            # 3つの単語のアナロジーの場合
            match = analogy_pattern.match(line)
            if match:
                word1, word2, word3, _ = match.groups() # 4つ目の単語は無視
                result_word, similarity = manager.analogy(word1, word2, word3)
                if result_word and similarity is not None:
                    results.append(f"{section_name} {line} {result_word} {similarity:.4f}")
                else:
                    results.append(f"{section_name} {line} None None")
            else:
                # パターンに一致しない行（エラーケース）
                results.append(f"{section_name} {line} ERROR INVALID_FORMAT")

    return results

def main():
    model_path = "data/GoogleNews-vectors-negative300.bin"
    analogy_file_path = "data/questions-words.txt"
    output_file_path = "ans64.txt"

    manager = WordVectorManager(model_path)

    try:
        manager.load_model()
        results = process_analogy_file(analogy_file_path, manager)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            for line in results:
                f.write(f"{line}\n")

        logging.info(f"結果を {output_file_path} に書き込みました")

    except FileNotFoundError as e:
        logging.error(f"ファイルが見つかりません: {e}")
    except ValueError as e:
        logging.error(f"モデルの読み込みエラー: {e}")
    except Exception as e:
        logging.error(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()