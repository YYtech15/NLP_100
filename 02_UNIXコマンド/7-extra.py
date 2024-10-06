# 7.py 
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルをN個のファイルに分割せよ．

import sys
import math

def save_split_file(file_name: str, N: int) -> None:
    with open(f"{file_name}.txt", "r") as input_f:
        lines = input_f.readlines()
        
    total_lines = len(lines)
    # N分割したときの1つあたりの行数（端数は切り上げ）
    chunk_size = math.ceil(total_lines / N)
    
    for i in range(N):
        start = i * chunk_size
        end = start + chunk_size
        chunk_lines = lines[start:end]
        with open(f"{file_name}_{i+1}.txt", "w") as output_f:
            output_f.writelines(chunk_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_name> <N>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    N = int(sys.argv[2])
    
    save_split_file(file_name, N)