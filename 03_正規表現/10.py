# 10.py 
# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，
# ファイル参照をURLに変換すればよい）
import re
import requests
from typing import Dict, Optional, Tuple

# Constants
INPUT_FILE = 'uk_article.txt'
OUTPUT_FILE = 'basic_info_with_flag_url.txt'
BASIC_INFO_PATTERN = re.compile(r'\{\{基礎情報.*?\n(.*?)\n\}\}', re.DOTALL)
FIELD_PATTERN = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\||\n$)', re.DOTALL)
EMPHASIS_PATTERN = re.compile(r"'{2,5}")
INTERNAL_LINK_PATTERN = re.compile(r'\[\[(?:[^|]*?\|)?([^|]*?)\]\]')
FILE_PATTERN = re.compile(r'\[\[(ファイル|File):([^|]+).*\]\]')

API_ENDPOINT = "https://ja.wikipedia.org/w/api.php"

def remove_markup(text: str) -> str:
    """Remove simple MediaWiki markup from text."""
    text = EMPHASIS_PATTERN.sub('', text)
    text = INTERNAL_LINK_PATTERN.sub(r'\1', text)
    return text.strip()

def extract_basic_info(content: str) -> Dict[str, str]:
    """Extract basic info from content."""
    match = BASIC_INFO_PATTERN.search(content)
    if not match:
        return {}

    basic_info_content = match.group(1)
    fields = FIELD_PATTERN.findall(basic_info_content)
    
    return {
        remove_markup(field_name): remove_markup(value)
        for field_name, value in fields
    }

def get_image_url(file_name: str) -> Optional[str]:
    """
    Get the URL of an image using the MediaWiki API.

    Args:
        file_name (str): The name of the image file.

    Returns:
        Optional[str]: The URL of the image, or None if not found.
    """
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": f"File:{file_name}"
    }

    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        imageinfo = page.get("imageinfo")
        if imageinfo:
            return imageinfo[0].get("url")
    
    return None

def extract_flag_info(basic_info: Dict[str, str]) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract flag file name and get its URL.

    Args:
        basic_info (Dict[str, str]): The basic info dictionary.

    Returns:
        Tuple[Optional[str], Optional[str]]: The flag file name and its URL.
    """
    flag_value = basic_info.get("国旗画像")
    if not flag_value:
        return None, None

    match = FILE_PATTERN.search(flag_value)
    if not match:
        return flag_value, None

    file_name = match.group(2)
    url = get_image_url(file_name)
    return file_name, url

def read_file(file_name: str) -> Optional[str]:
    """Read the content of a file."""
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {file_name}: {e}")
        return None

def write_output(data: Dict[str, str], flag_info: Tuple[Optional[str], Optional[str]], output_file: str) -> None:
    """Write processed data to output file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for field_name, value in data.items():
                f.write(f'{field_name}: {value}\n')
            
            f.write("\n--- Flag Information ---\n")
            f.write(f"Flag file name: {flag_info[0] or 'Not found'}\n")
            f.write(f"Flag URL: {flag_info[1] or 'Not found'}\n")
        
        print(f"Data written to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main() -> None:
    """Main function to orchestrate the process."""
    content = read_file(INPUT_FILE)
    if content is None:
        return

    basic_info = extract_basic_info(content)
    if not basic_info:
        print("No basic info found.")
        return

    flag_info = extract_flag_info(basic_info)
    write_output(basic_info, flag_info, OUTPUT_FILE)
    print(f"Extracted {len(basic_info)} fields from basic info template.")
    print(f"Flag file: {flag_info[0] or 'Not found'}")
    print(f"Flag URL: {flag_info[1] or 'Not found'}")

if __name__ == '__main__':
    main()