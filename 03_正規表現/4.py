# 4.py
# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル
# （例えば”== セクション名 ==”なら1）を表示せよ．
# == セクション名 == は レベル1 のセクション（最上位のセクション）
# === セクション名 === は レベル2 のセクション（その下の階層）
# ==== セクション名 ==== は レベル3 のセクション（さらに下の階層）
import re
from typing import List, Tuple, Optional

# Constants
INPUT_FILE = "uk_article.txt"
OUTPUT_FILE = "section_structure.txt"
SECTION_PATTERN = re.compile(r'^(={2,})\s*(.+?)\s*\1$', re.MULTILINE)

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

def get_section_level(section_markers: str) -> int:
    """
    Calculate the section level based on the number of '=' characters.

    Args:
        section_markers (str): The '=' characters surrounding the section title.

    Returns:
        int: The section level.
    """
    return len(section_markers) - 2

def extract_section_structure(content: str) -> List[Tuple[str, int]]:
    """
    Extract section names and their levels from the given content.

    Args:
        content (str): The content to extract section structure from.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing section names and their levels.
    """
    return [(match.group(2), get_section_level(match.group(1))) 
            for match in SECTION_PATTERN.finditer(content)]

def write_output(section_structure: List[Tuple[str, int]], output_file: str) -> None:
    """
    Write the extracted section structure to a file.

    Args:
        section_structure (List[Tuple[str, int]]): The section structure to write.
        output_file (str): The path to the output file.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for section_name, section_level in section_structure:
                f.write(f"{section_name}: {section_level}\n")
        print(f"Section structure saved to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main() -> None:
    """Main function to orchestrate the section structure extraction process."""
    content = read_file(INPUT_FILE)
    if content is None:
        return

    section_structure = extract_section_structure(content)
    if section_structure:
        write_output(section_structure, OUTPUT_FILE)
    else:
        print("No sections found.")

if __name__ == "__main__":
    main()