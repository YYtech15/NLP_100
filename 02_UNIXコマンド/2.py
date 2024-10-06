# 2.py 
# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

'''
sedコマンド
sed 's/\t/ /g' popular-names.txt > output.txt

s/\t/ /g は「すべてのタブ文字をスペースに置換すること」を意味
s/元のパターン/置換後の文字列/フラグ
元のパターン：\t
置換後の文字列: (スペース)
フラグ:global / 全体置換
'''

'''
trコマンド
tr '\t' ' ' < popular-names.txt > output.txt

'\t' ' ' は「タブ文字をスペースに置換すること」を意味
'''

'''
expandコマンド
expand -t 1 popular-names.txt > output.txt

-t 1 は「1タブを1スペースに置換すること」を意味
'''

def replace_tab_with_space(file_name: str, output_file_name: str) -> None:
    # result = []
    # with open(f"{file_name}.txt", "r") as lines:
    #     for line in lines:
    #         result.append(line.replace("\t", " "))
    # return "".join(result)
    
    with open(f"{file_name}.txt", "r") as input_f, \
         open(f"{output_file_name}.txt", "w") as output_f:
    # 各行のタブをスペースに置換し、一つの文字列として返す
         content = input_f.read().replace("\t", " ")
         output_f.write(content)

if __name__ == "__main__":
    file_name = "popular-names"
    output_file_name = "output-popular-names"
    replace_tab_with_space(file_name, output_file_name)