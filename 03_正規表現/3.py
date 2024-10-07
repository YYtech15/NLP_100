import re
from typing import List

# カテゴリ名を抽出する関数
def extract_category_names(file_name: str) -> List[str]:
    category_pattern = re.compile(r'\[\[Category:(.*?|(\|.*)?)\]\]')
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()

    # 正規表現を使ってカテゴリ名をリストに格納
    return [match.group(1) for match in category_pattern.finditer(content)]

if __name__ == '__main__':
    file_name = 'uk_article.txt'
    category_names = extract_category_names(file_name)

    with open('category_names.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(category_names))
