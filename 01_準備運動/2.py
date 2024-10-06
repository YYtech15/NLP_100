# 2.py 
# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

def extract_odd_index_chars(word: str) -> str:
    return word[0::2]

if __name__ == "__main__":
    word = "パタトクカシーー"
    
    ans = extract_odd_index_chars(word)
    print("ans:", ans)
