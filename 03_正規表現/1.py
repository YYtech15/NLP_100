# 1.py 
# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，
# 「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．
import gzip
import json

# "イギリス"に関する記事本文を探す関数
def find_uk_article(file_path: str) -> None:
    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        for line in f:
            article = json.loads(line)
            if article["title"] == "イギリス":
                return article["text"]
    return None

if __name__ == "__main__":
    # gzip圧縮されたファイルのパス
    file_path = "jawiki-country.json.gz"
    # イギリスの記事本文を取得して表示
    uk_article = find_uk_article(file_path)

    if uk_article:
        with open("uk_article.txt", "w", encoding="utf-8") as f:
            f.write(uk_article)
        print("イギリスに関する記事本文をuk_article.txtに保存しました。")
    else:
        print("イギリスに関する記事が見つかりませんでした。")

