#coding:utf-8

from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen("http://xpresskitadmin.directed.com/firmwares.aspx").read()
soup = BeautifulSoup(url)


