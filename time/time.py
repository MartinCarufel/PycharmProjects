#coding:utf-8

from datetime import datetime

now = datetime.now()
print(now)


time_obj = datetime.now()
time_str = time_obj.strftime("%Y-%m-%d_%H%M%S")
print(time_str)
