# 5.py 
# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
import re
from typing import List

def extract_media_files(file_name: str) -> List[str]:
    media_pattern = re.compile(r'\[\[ファイル:(.*?)\|')
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    return media_pattern.findall(content)

if __name__ == '__main__':
    file_name = 'uk_article.txt'
    media_files = extract_media_files(file_name)
    with open('media_files.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(media_files))