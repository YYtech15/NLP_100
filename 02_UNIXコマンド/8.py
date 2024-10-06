# 8.py 
# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはcut, sort, uniqコマンドを用いよ．

'''
cut -f 1 popular-names.txt | sort | uniq

cut -f 1:

cut コマンド
    ファイルの特定の列を抽出するために使用
    -f 1 は1列目を抽出
    デフォルトではタブ文字区切り
    スペース区切りの場合は -d ' ' オプションを使用
    
sort コマンド
    出力結果をソート
    ※uniq コマンドはソートされたデータに対して重複を削除するので、sort は必須

uniq コマンド
    ソートされた結果から重複を削除し、1列目の異なる文字列の集合を返す
    
|（パイプ）
    コマンド同士をつなぎ、前のコマンドの出力を次のコマンドの入力として渡すために使用
'''

def unique_first_column(file_name: str) -> None:
    with open(f"{file_name}.txt", "r") as file:
        first_column_set = set()
        
        for line in file:
            first_column = line.split()[0]
            first_column_set.add(first_column)

    with open("unique_first_column.txt", "w") as f:
        for value in sorted(first_column_set):
            f.write(value + "\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    unique_first_column(file_name)
