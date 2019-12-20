#coding:utf-8

import os
import sys
import datetime
from subprocess import PIPE, Popen
import pyautogui
from time import sleep
import re

sys.path.append('C:/Drive-W/Internal_tools/Libraries/IOLibrary/trunk/out')
from IOWrapper import IOWrapper

def create_log():
    currentDateTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = currentDateTime + ".log"
    currentdir = os.getcwd()
    path = os.path.join(currentdir, "report", filename)

    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return(path)


def process(line, *args):
    timestamp = 0.0

    for i in args:
        regSearch = re.search(i, line)
        if regSearch:
            #logfile.write("Got it!\n")
            timestamp = line.split(":")
            timestamp = timestamp[0]
            break
    return timestamp


def start_d2d2_sniffer():
    commands = ["start", "cmd", "/k"]
    p = Popen(commands, shell=True, stdin=PIPE, stdout=PIPE, universal_newlines=True)
    sleep(0.3)
    title = pyautogui.getWindow("system32")
    title.set_foreground()
    pyautogui.typewrite("cd sniffer\n")
    pyautogui.typewrite("d2d2_sniffer /port=COM2\n")
    return p



##################################################################
# MAIN
####################################################################


inputDev = IOWrapper()
inputDev.IO_Connect_Device(1, "COM5")
outputDev = IOWrapper()
outputDev.IO_Connect_Device(2, "COM10")
outputDev.IO_Read_Map("DS4_Analog_Harness_3.xml")

mypath = create_log()
logfile = open(mypath, 'w')
currentDateTime = datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")
logfile.write(currentDateTime + " - Test Start\n")

p = start_d2d2_sniffer()
pyautogui.typewrite("/log reset_ble.log\n")
outputDev.IO_Set_Value("siren_pwr", True)
sleep(5)

pyautogui.typewrite("/send 22 10 92\n")
sleep(6)

outputDev.IO_Set_Value("siren_pwr", False)
sleep(60)  #wait 16 minutes

outputDev.IO_Set_Value("ignition", True)
sleep(2)
outputDev.IO_Set_Value("brake", True)
sleep(1)
outputDev.IO_Set_Value("brake", False)

outputDev.IO_Set_Value("ignition", False)
sleep(1)

pyautogui.typewrite("/log close\n")
pyautogui.typewrite("/q\n")
sleep(10)
outputDev.IO_Set_Value("siren_pwr", False)
outputDev.IO_Set_Value("ignition", False)


lineTimeCompare = []

checkBrakeOn = r'SET_BRAKE_ON'
checkBrakeOff = r'SET_BRAKE_OFF'
#checkResetBle = r'AID .. 6C 49 A5 02 44 45 49 2D 42 4C 45 20 00 00 00 00'

with open(".\\sniffer\\reset_ble.log", "r") as f:
    for line in f:
        #temp = process(line, checkBrakeOn, checkResetBle)
        temp = process(line, checkBrakeOn, checkBrakeOff)

        if temp != 0.0:
            lineTimeCompare.append(temp)



inputDev.IO_Disconnect()
outputDev.IO_Disconnect()


try:
    difftime = float(lineTimeCompare[1]) - float(lineTimeCompare[0])
    print("Result de l'operation :{}".format(difftime))
    resultValid = True


except IndexError:
    resultValid = False
    currentDateTime = datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")
    logfile.write(currentDateTime + " - Reset BLE FAILED\n")
    print("No reset occur")

if resultValid:
    if difftime < 5:
        currentDateTime = datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")
        logfile.write(currentDateTime + "- Reset BLE PASS\n")
    else:
        currentDateTime = datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")
        logfile.write(currentDateTime + " - Reset BLE FAILED\n")


title = pyautogui.getWindow("system32")
title.set_foreground()
pyautogui.keyDown("altleft")
pyautogui.press("f4")
pyautogui.keyUp("altleft")

p.kill()