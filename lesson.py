# ライブラリのインポート
import requests

# URLの設定
url = "https://www.python.org"

# サイトにアクセス
r = requests.get(url)
print(r)