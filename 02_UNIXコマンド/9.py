# 9.py 
# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ
# （注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ
# （この問題はコマンドで実行した時の結果と合わなくてもよい）．

'''
sortコマンド
sort -k 3,3nr file_name.txt

-k 3,3: 3列目を基準にソートすることを指定。3,3 は「開始列と終了列を3列目に指定」という意味
n: 数値としてソートすることを指定
r: 降順（逆順）にソート
'''

import sys

def sort_by_third_column(file_name: str) -> None:
    with open(f"{file_name}.txt", "r") as file:
        lines = file.readlines()
    
    # 3列目（数値）の降順でソート
    '''    
    key=lambda line: int(line.split()[2])
    
    key
        - sorted() 関数に渡すオプション。key に与えた関数は各要素に対して適用され、その結果に基づいてソート

    lambda line: int(line.split()[2])
        - 無名関数（ラムダ式）。この関数はリストの各要素（ここでは行）に対して適用
        - lineという引数を取り、その行の3列目の値をintで返す関数を定義
    '''
    sorted_lines = sorted(lines, key=lambda line: int(line.split()[2]), reverse=True)

    with open(f"{file_name}_sorted_by_third.txt", "w") as output_f:
        output_f.writelines(sorted_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    sort_by_third_column(file_name)
