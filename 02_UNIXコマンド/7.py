# 7.py 
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

'''
splitコマンド
split -l LINES file_name prefix --additional-suffix=.txt

-l LINES: 分割したい行数を指定。指定した行数ごとにファイルを分割
file_name: 分割するファイル名
prefix: 出力されるファイルの名前のプレフィックス
--additional-suffix=.txt: 各分割ファイルに .txt という拡張子を付ける

(例)split -l 200 popular-names.txt part_ --additional-suffix=.txt
'''

import sys

def save_split_file(file_name: str, N: int) -> None:
    with open(f"{file_name}.txt", "r") as input_f:
        lines = input_f.readlines()
        
    total_lines = len(lines)
  
    for i in range(0, total_lines, N):
        chunk_lines = lines[i:i+N]
        # 分割ファイルの名前を作成
        with open(f"{file_name}_part_{i+1}_{i+N}.txt", "w") as output_f:
            output_f.writelines(chunk_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_name> <N>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    N = int(sys.argv[2])
    
    save_split_file(file_name, N)