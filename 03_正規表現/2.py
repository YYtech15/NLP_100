# 2.py 
# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ

import re
from typing import List, Optional

# Constants
INPUT_FILE = "uk_article.txt"
OUTPUT_FILE = "category_lines.txt"
CATEGORY_PATTERN = re.compile(r"\[\[Category:.*?\]\]")

def read_file(file_path: str) -> Optional[str]:
    """
    Read the content of a file.

    Args:
        file_path (str): Path to the file to read.

    Returns:
        Optional[str]: The content of the file, or None if an error occurred.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def extract_category_lines(content: str) -> List[str]:
    """
    Extract category lines from the given content.

    Args:
        content (str): The content to extract categories from.

    Returns:
        List[str]: A list of extracted category lines.
    """
    return CATEGORY_PATTERN.findall(content)

def write_output(lines: List[str], output_file: str) -> None:
    """
    Write the extracted category lines to a file.

    Args:
        lines (List[str]): The lines to write.
        output_file (str): The path to the output file.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Category lines saved to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main() -> None:
    """Main function to orchestrate the category extraction process."""
    content = read_file(INPUT_FILE)
    if content is None:
        return

    category_lines = extract_category_lines(content)
    if category_lines:
        write_output(category_lines, OUTPUT_FILE)
    else:
        print("No category lines found.")

if __name__ == "__main__":
    main()