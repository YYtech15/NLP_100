# 4.py 
# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

'''
pasteコマンド
デフォルトではタブ区切りで結合
    -d オプションを使うと区切り文字を変更可能
    (例)paste -d ',' col1.txt col2.txt > merged.csv

paste col1.txt col2.txt > merged.txt
'''

def merge_columns(col1_file: str, col2_file: str, output_file: str) -> None:
    with open(f"{col1_file}.txt", "r") as col_1, \
        open(f"{col2_file}.txt", "r") as col_2, \
        open(f"{output_file}.txt", "w") as output_f:
        
            for line1, line2 in zip(col_1, col_2):
                output_f.write(f"{line1.strip()}\t{line2.strip()}\n")

if __name__ == "__main__":
    col1_file = "col1"
    col2_file = "col2"
    output_file_name = "merged"
    merge_columns(col1_file, col2_file, output_file_name)