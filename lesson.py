# ライブラリをインポート
import requests
import schedule
import time
from bs4 import BeautifulSoup

def tracking():
  # url
  url = "https://to-do.live.com/tasks/"
  res = requests.get(url)

  soup = BeautifulSoup(res.content, 'html.parser')
  title = soup.find('div',class_="grid")
  print(title)

tracking()

  # if(title == title):
  #   print("通知")
    # sendLineNotify()

# def sendLineNotify():
#   token = "ICYGOgmSgUMKJLidi0ZLsATqFiaNzU0zPW2hOY0BlQJ"
#   notifyApi = "https://notify-api.line.me/api/notify"
#   headers = {"Authorization" : f"Bearer {token}"}
#   data = {"message" : "task is change https://www.yahoo.co.jp/"}
#   requests.post(notifyApi, headers=headers, data=data)

# schedule.every(5).seconds.do(tracking)

# while True:
#   schedule.ran_pending()
#   time.sleep(1)