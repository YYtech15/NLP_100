# 6.py 
# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

'''
tailコマンド
tail -n N file_name

-n N: 表示したい行数を指定。N行目までを表示
file_name: 表示したいファイルの名前
'''

import sys

def print_tail(file_name: str, N: int) -> None:
    with open(f"{file_name}.txt", "r") as f:
        lines = f.readlines()
        tail_lines = lines[-N:]
        for line in tail_lines:
            print(line, end="")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_name> <N>")
        sys.exit(1)
    file_name = sys.argv[1]
    N = int(sys.argv[2])
    
    print_tail(file_name, N)