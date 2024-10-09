# 9.py 
# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを
# 可能な限り除去し，国の基本情報を整形せよ．
import re
from typing import Dict, Optional

# Constants
INPUT_FILE = 'uk_article.txt'
OUTPUT_FILE = 'basic_info_cleaned.txt'
BASIC_INFO_PATTERN = re.compile(r'\{\{基礎情報.*?\n(.*?)\n\}\}', re.DOTALL)
FIELD_PATTERN = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\||\n$)', re.DOTALL)
EMPHASIS_PATTERN = re.compile(r"'{2,5}")
INTERNAL_LINK_PATTERN = re.compile(r'\[\[(?:[^|]*?\|)?([^|]*?)\]\]')
EXTERNAL_LINK_PATTERN = re.compile(r'\[(?:https?://)?(?:[^\s\]]+?\s)?([^\]]+?)\]')
HTML_TAG_PATTERN = re.compile(r'<.*?>')
CITATION_PATTERN = re.compile(r'<ref>.*?</ref>')
TEMPLATE_PATTERN = re.compile(r'\{\{.*?\}\}')
COMMENT_PATTERN = re.compile(r'<!--.*?-->', re.DOTALL)

def remove_markup(text: str) -> str:
    """
    Remove all MediaWiki markup from text.

    Args:
        text (str): The text to remove markup from.

    Returns:
        str: The text with all markup removed.
    """
    text = EMPHASIS_PATTERN.sub('', text)
    text = INTERNAL_LINK_PATTERN.sub(r'\1', text)
    text = EXTERNAL_LINK_PATTERN.sub(r'\1', text)
    text = HTML_TAG_PATTERN.sub('', text)
    text = CITATION_PATTERN.sub('', text)
    text = TEMPLATE_PATTERN.sub('', text)
    text = COMMENT_PATTERN.sub('', text)
    return text.strip()

def extract_basic_info(content: str) -> Dict[str, str]:
    """
    Extract basic info from content and remove MediaWiki markup.

    Args:
        content (str): The content to extract basic info from.

    Returns:
        Dict[str, str]: A dictionary containing the extracted and cleaned basic info.
    """
    match = BASIC_INFO_PATTERN.search(content)
    if not match:
        return {}

    basic_info_content = match.group(1)
    fields = FIELD_PATTERN.findall(basic_info_content)
    
    return {
        remove_markup(field_name): remove_markup(value)
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
    """Main function to orchestrate the basic info extraction and cleaning process."""
    content = read_file(INPUT_FILE)
    if content is None:
        return

    basic_info = extract_basic_info(content)
    if basic_info:
        write_output(basic_info, OUTPUT_FILE)
        print(f"Extracted and cleaned {len(basic_info)} fields from basic info template.")
    else:
        print("No basic info found.")

if __name__ == '__main__':
    main()