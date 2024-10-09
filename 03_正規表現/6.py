import re
from typing import Dict, Optional

# Constants
INPUT_FILE = 'uk_article.txt'
OUTPUT_FILE = 'basic_info.txt'
BASIC_INFO_PATTERN = re.compile(r'\{\{基礎情報.*?\n(.*?)\n\}\}', re.DOTALL)
FIELD_PATTERN = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\||\n$)', re.DOTALL)

def extract_basic_info(content: str) -> Dict[str, str]:
    """
    Extract basic info from the given content.
    
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

    return {field_name.strip(): value.strip() for field_name, value in fields}

def read_file(file_name: str) -> Optional[str]:
    """
    Read the content of a file.
    
    Args:
        file_name (str): The name of the file to read.
    
    Returns:
        Optional[str]: The content of the file, or None if the file is not found.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return None

def write_output(data: Dict[str, str], output_file: str) -> None:
    """
    Write the extracted basic info to an output file.
    
    Args:
        data (Dict[str, str]): The data to write.
        output_file (str): The name of the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for field_name, value in data.items():
            f.write(f'{field_name}: {value}\n')

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