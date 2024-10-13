# 5.py 
# 64. アナロジーデータでの実験
# 単語アナロジーの評価データをダウンロードし，
# vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
# そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
# 求めた単語と類似度は，各事例の末尾に追記せよ．
import re
import logging
import seven_lib
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_analogy_file(file_path: str, manager: seven_lib.WordVectorManager) -> List[str]:
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
    compressed_path = "data/GoogleNews-vectors-negative300.bin.gz"
    decompressed_path = "data/GoogleNews-vectors-negative300.bin"
    analogy_file_path = "data/questions-words.txt"
    output_file_path = "ans64.txt"

    manager = seven_lib.WordVectorManager(compressed_path, decompressed_path)

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