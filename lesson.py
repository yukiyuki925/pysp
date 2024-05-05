# ライブラリをインポート
import requests
import schedule
import time
from bs4 import BeautifulSoup

switch = False

def tracking():
  # url
  url = "https://www.yahoo.co.jp/"
  res = requests.get(url)

  soup = BeautifulSoup(res.content, 'html.parser')
  title = soup.select("div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-of-type(4)")[0].get_text()
  # print(title)

  last_title = ""

  try:
      with open("last_title.txt", "r") as file:
        last_title = file.read()
  except FileNotFoundError:
      pass


  if(title != last_title):
    print("通知")
    sendLineNotify()

  with open("last_title.txt", "w") as file:
      file.write(title)


def sendLineNotify():
  global switch
  token = "ICYGOgmSgUMKJLidi0ZLsATqFiaNzU0zPW2hOY0BlQJ"
  notifyApi = "https://notify-api.line.me/api/notify"
  headers = {"Authorization" : f"Bearer {token}"}
  data = {"message" : "news is change https://www.yahoo.co.jp/"}
  requests.post(notifyApi, headers=headers, data=data)
  switch = True

schedule.every(5).seconds.do(tracking)

while True:
  schedule.run_pending()
  time.sleep(1)

  if switch == True:
    switch = False
    break
