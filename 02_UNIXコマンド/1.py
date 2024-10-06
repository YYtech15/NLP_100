# 1.py 
# 10. 行数のカウントPermalink
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# 確認コマンド：wc -l popular-names.txt
# 結果：2779 popular-names.txt

# od -c popular-names.txt | tail -n 2
# -cオプションを使うと、ファイルをASCII文字として出力
# 0160660   4   3   5  \t   2   0   1   8  \r  \n   L   o   g   a   n  \t
# 0160700   M  \t   1   2   3   5   2  \t   2   0   1   8
# 0160714

# wcコマンドは改行(\n)の数を数える→最後に\nがないので、1行分数えられていない
# 行数：2780


def count_lines_in_file(file_name: str) -> int:
    """
    指定されたファイルの行数をカウントする関数。

    :param file_name: ファイル名（拡張子を含まない）
    :return: 行数
    """
    with open(f"{file_name}.txt", "r") as file:
        return sum(1 for _ in file) # それぞれの行に対して1を返し、その合計を取得

if __name__ == "__main__":
    file_name = "popular-names"
    ans = count_lines_in_file(file_name)
    print("ans:", ans)