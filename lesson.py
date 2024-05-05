# ライブラリをインポート
import requests
import schedule
import time
from bs4 import BeautifulSoup

def tracking():
  # url
  url = "https://www.yahoo.co.jp/"
  res = requests.get(url)

  soup = BeautifulSoup(res.content, 'html.parser')
  title = soup.select("div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-of-type(4)")[0].get_text()

  if(title != title):
    print("通知")
    sendLineNotify()

def sendLineNotify():
  token = "ICYGOgmSgUMKJLidi0ZLsATqFiaNzU0zPW2hOY0BlQJ"
  notifyApi = "https://notify-api.line.me/api/notify"
  headers = {"Authorization" : f"Bearer {token}"}
  data = {"message" : "news is change https://www.yahoo.co.jp/"}
  requests.post(notifyApi, headers=headers, data=data)

schedule.every(5).seconds.do(tracking)

while True:
    schedule.run_pending()
    time.sleep(1)