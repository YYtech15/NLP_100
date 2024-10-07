# 4.py
# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル
# （例えば”== セクション名 ==”なら1）を表示せよ．
# == セクション名 == は レベル1 のセクション（最上位のセクション）
# === セクション名 === は レベル2 のセクション（その下の階層）
# ==== セクション名 ==== は レベル3 のセクション（さらに下の階層）
import re

def get_section_level(section):
    return len(section) - 1

def get_section_name(section):
    return section.strip("=")

def extract_section_structure(file_name: str):
    section_pattern = re.compile(r'(={2,})(.*?)(={2,})')
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()

    # 正規表現を使ってセクション名とレベルを抽出
    return [(get_section_name(match.group(2)), get_section_level(match.group(1))) for match in section_pattern.finditer(content)]

if __name__ == "__main__":
    file_name = "uk_article.txt"
    section_structure = extract_section_structure(file_name)

    with open("section_structure.txt", "w", encoding="utf-8") as f:
        for section_name, section_level in section_structure:
            f.write(f"{section_name}: {section_level}\n")