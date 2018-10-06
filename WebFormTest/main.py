#coding:utf-8
import re
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)
url = "http://xpresskitadmin.directed.com/firmwares.aspx"
browser.open(url)

form =browser.get_form(action = "./firmwares.aspx")
form
form['ctl00$MainContentPlaceHolder$ctl00$tbFilterFirmware'] = "honda7"
browser.submit_form(form)

