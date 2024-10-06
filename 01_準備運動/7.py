# 7.py 
# 06. 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
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

def set_operations(X, Y):
    #　和集合
    union = X | Y
    # 積集合
    intersection = X & Y
    # 差集合
    difference = X - Y
    
    return union, intersection, difference

def check_bigram(bigram, X, Y):
    return bigram in X, bigram in Y

if __name__ == "__main__":
    text_1 = "paraparaparadise"
    text_2 = "paragraph"
    
    # 文字bi-gram
    X = set(generate_n_grams(text_1, 2, gram_type="char"))
    Y = set(generate_n_grams(text_2, 2, gram_type="char"))
    
    # 和集合, 積集合, 差集合を計算
    union, intersection, difference = set_operations(X, Y)
    
    print("X:", sorted(X))  
    print("Y:", sorted(Y))  
    print("和集合 (Union):", sorted(union))  
    print("積集合 (Intersection):", sorted(intersection))  
    print("差集合 (Difference):", sorted(difference))  
    
    # 'se'がXおよびYに含まれているかをチェック
    bigram = 'se'
    in_X, in_Y = check_bigram(bigram, X, Y)
    
    print(f"'{bigram}' in X:", in_X)
    print(f"'{bigram}' in Y:", in_Y)
