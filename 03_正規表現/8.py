# 8.py 
# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値から
# MediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ（参考: マークアップ早見表）．
import re
from typing import Dict, Optional

# Constants
INPUT_FILE = 'uk_article.txt'
OUTPUT_FILE = 'basic_info_removed_link.txt'
BASIC_INFO_PATTERN = re.compile(r'\{\{基礎情報.*?\n(.*?)\n\}\}', re.DOTALL)
FIELD_PATTERN = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\||\n$)', re.DOTALL)
EMPHASIS_PATTERN = re.compile(r"'{2,5}")
INTERNAL_LINK_PATTERN = re.compile(r'\[\[(?:[^|]*?\|)?([^|]*?)\]\]')

def remove_emphasis(text: str) -> str:
    """
    Remove emphasis markup from text.

    Args:
        text (str): The text to remove emphasis from.

    Returns:
        str: The text with emphasis markup removed.
    """
    return EMPHASIS_PATTERN.sub('', text)

def remove_internal_link(text: str) -> str:
    """
    Remove internal link markup from text.

    Args:
        text (str): The text to remove internal links from.

    Returns:
        str: The text with internal link markup removed.
    """
    return INTERNAL_LINK_PATTERN.sub(r'\1', text)

def remove_markup(text: str) -> str:
    """
    Remove all markup from text.

    Args:
        text (str): The text to remove all markup from.

    Returns:
        str: The text with all markup removed.
    """
    text = remove_emphasis(text)
    text = remove_internal_link(text)
    return text

def extract_basic_info(content: str) -> Dict[str, str]:
    """
    Extract basic info from content.

    Args:
        content (str): The content to extract basic info from.

    Returns:
        Dict[str, str]: A dictionary containing the extracted basic info.
    """
    match = BASIC_INFO_PATTERN.search(content)
    if not match:
        return {}

    basic_info_content = match.group(1)
    fields = FIELD_PATTERN.findall(basic_info_content)
    
    return {
        remove_markup(field_name.strip()): remove_markup(value.strip())
        for field_name, value in fields
    }

def read_file(file_name: str) -> Optional[str]:
    """
    Read the content of a file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        Optional[str]: The content of the file, or None if an error occurred.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {file_name}: {e}")
        return None

def write_output(data: Dict[str, str], output_file: str) -> None:
    """
    Write processed data to output file.

    Args:
        data (Dict[str, str]): The data to write.
        output_file (str): The name of the output file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for field_name, value in data.items():
                f.write(f'{field_name}: {value}\n')
        print(f"Data written to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main() -> None:
    """Main function to orchestrate the basic info extraction process."""
    content = read_file(INPUT_FILE)
    if content is None:
        return

    basic_info = extract_basic_info(content)
    if basic_info:
        write_output(basic_info, OUTPUT_FILE)
        print(f"Extracted {len(basic_info)} fields from basic info template.")
    else:
        print("No basic info found.")

if __name__ == '__main__':
    main()