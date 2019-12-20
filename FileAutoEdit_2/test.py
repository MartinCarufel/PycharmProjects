#coding:utf-8

import os
import shutil
import tkinter.filedialog
import csv



out = open('out.csv', 'w')

with open('testfile.csv') as fp:
    for line in fp:
        out.write(line)
        print(line)