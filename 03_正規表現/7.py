# 7.py 
# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの
# 強調マークアップ（弱い強調，強調，強い強調のすべて）を除去して
# テキストに変換せよ（参考: マークアップ早見表）
import re
from typing import Dict, Optional

# Constants
INPUT_FILE = 'uk_article.txt'
OUTPUT_FILE = 'basic_info_removed_emphasis.txt'
BASIC_INFO_PATTERN = re.compile(r'\{\{基礎情報.*?\n(.*?)\n\}\}', re.DOTALL)
FIELD_PATTERN = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\||\n$)', re.DOTALL)
EMPHASIS_PATTERN = re.compile(r"'{2,5}")

def remove_emphasis_markup(text: str) -> str:
    """Remove emphasis markup from the given text."""
    return EMPHASIS_PATTERN.sub('', text)

def extract_basic_info(content: str) -> Dict[str, str]:
    """Extract basic info from the given content."""
    match = BASIC_INFO_PATTERN.search(content)
    if not match:
        return {}

    basic_info_content = match.group(1)
    fields = FIELD_PATTERN.findall(basic_info_content)

    return {
        remove_emphasis_markup(field_name.strip()): remove_emphasis_markup(value.strip())
        for field_name, value in fields
    }

def process_file(file_name: str) -> Optional[Dict[str, str]]:
    """Process the input file and return extracted information."""
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        return extract_basic_info(content)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return None

def write_output(data: Dict[str, str], output_file: str) -> None:
    """Write processed data to the output file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for field_name, value in data.items():
            f.write(f'{field_name}: {value}\n')

def main() -> None:
    """Main function to orchestrate the process."""
    basic_info = process_file(INPUT_FILE)

    if basic_info:
        write_output(basic_info, OUTPUT_FILE)
        print(f"Extracted {len(basic_info)} fields from basic info template.")
    else:
        print("No basic info found or an error occurred.")

if __name__ == '__main__':
    main()