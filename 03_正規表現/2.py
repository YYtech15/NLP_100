import re
from typing import List

def extract_category_lines(file_name: str) -> List[str]:
    category_pattern = re.compile(r"\[\[Category:.*\]\]")
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()

    # 正規表現を使ってカテゴリ行を抽出
    return category_pattern.findall(content)

if __name__ == "__main__":
    file_name = "uk_article.txt"
    category_lines = extract_category_lines(file_name)

    with open("category_lines.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(category_lines))
