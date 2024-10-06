# 6.py 
# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
import re

def generate_n_grams(text, n, gram_type="word"):
    """
    テキストからn-gramを生成する関数。

    :param text: 対象のテキスト（文字列）
    :param n: n-gramのn値
    :param gram_type: "word"の場合は単語n-gram、"char"の場合は文字n-gramを生成
    :return: n-gramのリスト
    """
    if gram_type == "word":
        words = re.sub(r"[^\w\s]","",text).split()
        n_grams = [words[i:i+n] for i in range(len(words) - n + 1)]
    elif gram_type == "char":
        chars = re.sub(r"[^\w]","",text)
        n_grams = [chars[i:i+n] for i in range(len(chars) - n + 1)]
    else:
        return "you select wrong gran_type"
    return n_grams
    
if __name__ == "__main__":
    text = "I am an NLPer"
    
    # 単語bi-gram
    word_bi_grams = generate_n_grams(text, 2, gram_type="word")
    print("Word bi-gram:", word_bi_grams)
    
    # 文字bi-gram
    char_bi_grams = generate_n_grams(text, 2, gram_type="char")
    print("Character bi-gram:", char_bi_grams)