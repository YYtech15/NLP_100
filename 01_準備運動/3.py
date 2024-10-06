# 3.py 
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def alternate_merge_strings(word_1: str, word_2: str) -> str:
    merge_words = ''.join([char_1 + char_2 for char_1, char_2 in zip(word_1, word_2)])
    return merge_words

if __name__ == "__main__":
    word_1 = "パトカー"
    word_2 = "タクシー"
    
    ans = alternate_merge_strings(word_1, word_2)
    print("ans:", ans)