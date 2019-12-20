#coding:utf-8

import os
import sys
import datetime
from subprocess import PIPE, Popen
import pyautogui
from time import sleep
import re




checkBrakeOn = r'SET_BRAKE_ON'
checkResetBle = r'AID .. 6C 49 A5 02 44 45 49 2D 42 4C 45 20 00 00 00 00'

with open(".\\sniffer\\test.log", "r") as f:
    for line in f:
        regSearch = re.search(checkResetBle, line)
        if (regSearch):
            print("Got it!")