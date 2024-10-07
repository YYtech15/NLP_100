# 7.py 
# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの
# 強調マークアップ（弱い強調，強調，強い強調のすべて）を除去して
# テキストに変換せよ（参考: マークアップ早見表）
import re

def remove_emphasis_markup(text: str) -> str:
    emphasis_pattern = re.compile(r"'{5}|'{3}|'{2}")
    return emphasis_pattern.sub('', text)

def extract_basic_info(file_name: str) -> dict:
    basic_info = {}
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()

        # 基礎情報テンプレートを抽出
        # 通常、正規表現の . は改行文字にマッチしないが、re.DOTALL を付けることで . が改行文字にもマッチするようになる
        basic_info_pattern = re.compile(r'\{\{基礎情報.*?\n(.*?)\n\}\}', re.DOTALL)
        match = basic_info_pattern.search(content)
        if not match:
            print("No basic info template found.")
            return basic_info

        # 基礎情報テンプレートの内容
        basic_info_content = match.group(1)

        # フィールド名と値を抽出
        # (?= ...) の使用
        # 特定のパターンの後に続く文字列の存在をチェック可能だが、チェックした部分は結果に含まれない
        fields = re.findall(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\||\n$)', basic_info_content, re.DOTALL)

        for field_name, value in fields:
            basic_info[remove_emphasis_markup(field_name).strip()] = remove_emphasis_markup(value).strip()

    except FileNotFoundError:
        print(f"Error: {file_name} not found.")

    return basic_info

if __name__ == '__main__':
    file_name = 'uk_article.txt'
    basic_info = extract_basic_info(file_name)

    if basic_info:
        with open('basic_info_removed_emphasis.txt', 'w', encoding='utf-8') as f:
            for field_name, value in basic_info.items():
                f.write(f'{field_name}: {value}\n')
        print(f"Extracted {len(basic_info)} fields from basic info template.")
    else:
        print("No basic info found or an error occurred.")
