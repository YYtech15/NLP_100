# 6.py 
# 65. アナロジータスクでの正解率
# 64の実行結果を用い，意味的アナロジー(semantic analogy)
# と文法的アナロジー(syntactic analogy)の正解率を測定せよ．
from typing import Dict, List, Tuple
from collections import defaultdict

def parse_line(line: str) -> Tuple[str, str, str]:
    parts = line.strip().split()
    if len(parts) != 7:
        return None
    return parts[0], parts[3], parts[5]  # category, answer, predicted

def calculate_accuracy(file_path: str) -> Dict[str, float]:
    results = defaultdict(lambda: {'correct': 0, 'total': 0})

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parsed = parse_line(line)
            if not parsed:
                continue

            category, answer, predicted = parsed
            analogy_type = 'syntactic' if category.startswith('gram') else 'semantic'
            results[analogy_type]['total'] += 1

            if answer == predicted:
                results[analogy_type]['correct'] += 1

    return {key: result['correct'] / result['total'] if result['total'] > 0 else 0
            for key, result in results.items()}

def main():
    file_path = "ans64.txt"

    try:
        accuracies = calculate_accuracy(file_path)

        print(f"意味的アナロジー(Semantic Analogy)の正解率: {accuracies['semantic']:.4f}")
        print(f"文法的アナロジー(Syntactic Analogy)の正解率: {accuracies['syntactic']:.4f}")

    except FileNotFoundError:
        print(f"ファイル '{file_path}' が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()