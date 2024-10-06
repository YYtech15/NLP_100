# 3.py 
# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

'''
cutコマンド
cut -f フィールド番号(列番号)ファイル名

-f オプションで抽出したい列を指定
デフォルトでタブ文字を区切り文字
    -d オプションを使うと、別の区切り文字を指定可能
    (例)cut -d ',' -f 1,2 data.csv
複数の列を抽出可能

cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt
'''

def save_columns(file_name: str, col1_file: str, col2_file: str) -> None:
    with open(f"{file_name}.txt", "r") as input_f, \
        open(f"{col1_file}.txt", "w") as col_1, \
        open(f"{col2_file}.txt", "w") as col_2:
        for line in input_f:
            columns = line.split("\t")
            if len(columns) >= 2:
                col_1.write(columns[0] + "\n")
                col_2.write(columns[1] + "\n")

if __name__ == "__main__":
    file_name = "popular-names"
    col1_file = "col1"
    col2_file = "col2"
    save_columns(file_name, col1_file, col2_file)