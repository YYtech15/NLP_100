# 3.py 
# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re
from typing import List, Optional

# Constants
INPUT_FILE = 'uk_article.txt'
OUTPUT_FILE = 'category_names.txt'
CATEGORY_PATTERN = re.compile(r'\[\[Category:([^|\]]+)(?:\|[^\]]+)?\]\]')

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

def extract_category_names(content: str) -> List[str]:
    """
    Extract category names from the given content.

    Args:
        content (str): The content to extract category names from.

    Returns:
        List[str]: A list of extracted category names.
    """
    return [match.group(1).strip() for match in CATEGORY_PATTERN.finditer(content)]

def write_output(lines: List[str], output_file: str) -> None:
    """
    Write the extracted category names to a file.

    Args:
        lines (List[str]): The lines to write.
        output_file (str): The path to the output file.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write('\n'.join(lines))
        print(f"Category names saved to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main() -> None:
    """Main function to orchestrate the category name extraction process."""
    content = read_file(INPUT_FILE)
    if content is None:
        return

    category_names = extract_category_names(content)
    if category_names:
        write_output(category_names, OUTPUT_FILE)
    else:
        print("No category names found.")

if __name__ == '__main__':
    main()
