#coding:utf-8

import io
import string

f = io.open("test_file.txt", "r")

cont = f.readlines()


for i in cont:
    print(string.printable)
    print (i)
