# 5.py 
# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
import re
from typing import List, Optional

# Constants
INPUT_FILE = 'uk_article.txt'
OUTPUT_FILE = 'media_files.txt'
MEDIA_PATTERN = re.compile(r'\[\[ファイル:(.*?)(?:\||\]\])')

def read_file(file_path: str) -> Optional[str]:
    """
    Read the content of a file.

    Args:
        file_path (str): Path to the file to read.

    Returns:
        Optional[str]: The content of the file, or None if an error occurred.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def extract_media_files(content: str) -> List[str]:
    """
    Extract media file names from the given content.

    Args:
        content (str): The content to extract media file names from.

    Returns:
        List[str]: A list of extracted media file names.
    """
    return MEDIA_PATTERN.findall(content)

def write_output(lines: List[str], output_file: str) -> None:
    """
    Write the extracted media file names to a file.

    Args:
        lines (List[str]): The lines to write.
        output_file (str): The path to the output file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Media file names saved to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main() -> None:
    """Main function to orchestrate the media file name extraction process."""
    content = read_file(INPUT_FILE)
    if content is None:
        return

    media_files = extract_media_files(content)
    if media_files:
        write_output(media_files, OUTPUT_FILE)
    else:
        print("No media files found.")

if __name__ == '__main__':
    main()