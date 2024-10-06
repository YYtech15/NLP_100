# 4.py 
# 03. 円周率
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import re

def word_lengths(sentence):
    # words = sentence.replace(",","").replace(".","").split()
    # 正規表現で句読点をすべて削除
    words = re.sub(r'[^\w\s]', '', sentence).split()
    return [len(word) for word in words]

if __name__ == "__main__":
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    
    ans = word_lengths(sentence)
    print("ans:", ans)