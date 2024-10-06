# 10.py 
# 19. 各行の1コラム目の文字列の出現頻度を求め，
# 出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，
# その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

'''
cut -f 1 popular-names.txt | sort | uniq -c | sort -nr

cut -f 1 popular-names.txt:
    cut コマンド
        ファイルの特定の列を抽出するために使用。
        -f 1 は1列目を抽出
            popular-names.txt の1列目だけが抽出されます。
sort:
    sort コマンド
        抽出された1列目をソート
        uniq コマンドが正しく動作するためには、データがソートされている必要あり
    
uniq -c:
    uniq コマンドに -c オプション
        重複する行の出現回数（カウント）を表示
        各文字列の出現回数が付加されたリストを取得

sort -nr:
    sort -nr は、数値 (n) と逆順 (r) でソートすることを意味
        出現頻度が高い順に並び替え
'''

import sys
from collections import Counter

def count_first_column_frequency(file_name: str) -> None:
    with open(f"{file_name}.txt", "r") as input_f:
        first_column_list = [line.split()[0] for line in input_f]  # 1列目を取得してリストに
    
    # 1列目の文字列の出現頻度をカウント
    # collections.Counter はリスト内の各要素が何回出現したかをカウントしてくれる便利なクラス
    first_column_count = Counter(first_column_list)
    # print(f"first_column_count:{first_column_count}")

    # 出現頻度の高い順に並べ替えて表示
    # Counter.most_common() メソッドは、出現頻度の高い順に要素を返す
    with open(f"{file_name}_sort_frequency.txt", "w") as output_f:
        for word, count in first_column_count.most_common():
            output_f.write(f"{word}: {count}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    count_first_column_frequency(file_name)
