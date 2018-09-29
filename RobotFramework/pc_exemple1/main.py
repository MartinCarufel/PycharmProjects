#coding:utf-8

import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)   # status code 200 on web page mean success
print(page.content)


page2 = requests.get("https://mail.google.com")
print(page.status_code)