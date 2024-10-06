# 9.py 
# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ
import re

def cipher(text: str) -> str:
    """
    与えられた文字列の各文字を、英小文字ならば (219 - 文字コード) に置換し、
    その他の文字はそのまま出力する関数。
    
    :param text: 入力された文字列
    :return: 暗号化または復号化された文字列
    """
    result = []
    for char in text:
        # 英小文字かどうかを判定
        if char.islower():
            # 219 - 文字コードの文字に置換
            result.append(chr(219 - ord(char)))
        else:
            # 英小文字でない場合はそのまま
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    message = "Hello, World!"
    encrypted_message = cipher(message)
    print("暗号化されたメッセージ:", encrypted_message)
    
    # 再度 cipher 関数を適用して復号化
    decrypted_message = cipher(encrypted_message)
    print("復号化されたメッセージ:", decrypted_message)