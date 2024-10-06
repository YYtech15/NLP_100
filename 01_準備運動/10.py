# 10.py 
# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
import random
import re

def typoglycemia(text: str) -> str:
    """
    スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、
    それ以外の文字をランダムに並び替える関数。

    :param text: 入力された文章
    :return: Typoglycemia処理後の文章
    """
    words = re.sub(r"[^\w\s':]", "", text).split()
    
    result = []
    
    for word in words:
        if len(word) <= 4:
            # 単語が4文字以下ならそのまま
            result.append(word)
        else:
            # 先頭と末尾の文字を除いてシャッフル
            middle = list(word[1:-1])
            random.shuffle(middle)
            shuffled_word = word[0] + ''.join(middle) + word[-1]
            result.append(shuffled_word)
    
    # スペースで結合して返す
    return ' '.join(result)

if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    
    ans = typoglycemia(text)
    print("ans:", ans)