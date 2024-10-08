# 1.py 
# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，
# 「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．
import gzip
import json
from typing import Optional

# Constants
INPUT_FILE = "jawiki-country.json.gz"
OUTPUT_FILE = "uk_article.txt"
TARGET_TITLE = "イギリス"

def find_article(file_path: str, target_title: str) -> Optional[str]:
    """
    Find an article with the specified title in the given gzipped JSON file.

    Args:
        file_path (str): Path to the gzipped JSON file.
        target_title (str): Title of the article to find.

    Returns:
        Optional[str]: The text of the found article, or None if not found.
    """
    try:
        with gzip.open(file_path, "rt", encoding="utf-8") as f:
            for line in f:
                article = json.loads(line)
                if article["title"] == target_title:
                    return article["text"]
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error processing file {file_path}: {e}")
    return None

def save_article(content: str, output_file: str) -> None:
    """
    Save the article content to a file.

    Args:
        content (str): The content to save.
        output_file (str): The path to the output file.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Article saved to {output_file}")
    except IOError as e:
        print(f"Error saving article to {output_file}: {e}")

def main() -> None:
    """Main function to orchestrate the article extraction process."""
    article_content = find_article(INPUT_FILE, TARGET_TITLE)

    if article_content:
        save_article(article_content, OUTPUT_FILE)
    else:
        print(f"No article found with title '{TARGET_TITLE}'.")

if __name__ == "__main__":
    main()

