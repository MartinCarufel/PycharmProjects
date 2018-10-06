#coding:utf-8

import os
import fnmatch

dirList = os.listdir("C:/Drive-W/Project/hk4/trunk/code/out/933")
print (dirList)
found = fnmatch.filter(dirList, "933.hk4.*")

encode = str("C:\\Jenkins\\workspace\\Flash_FW_HK4\\out\\933\\" + found[0])
print (encode)

