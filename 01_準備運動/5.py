# 5.py 
# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
import re
from typing import Dict

def extract_words(sentence: str) -> Dict[int,str]:
    # 先頭の1文字を取り出す単語の指定されている位置リスト
    first_char_pos = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    
    words = re.sub(r"[^\w\s]", "", sentence).split()
        
    result = {}
    for index, word in enumerate(words, start=1):
        if index in first_char_pos:
            result[index] = word[:1]
        else:
            result[index] = word[:2]
    return result 

if __name__ == "__main__":
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    
    ans = extract_words(sentence)
    print("ans:", ans)