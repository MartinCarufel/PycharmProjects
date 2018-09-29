#coding:utf-8

import sys
from time import sleep
import string
sys.path.append('C:/Drive-W/Internal_tools/Libraries/IOLibrary/trunk/out')
from IOWrapper import IOWrapper


io_mod = IOWrapper()
io_mod.IO_Connect_Device(1, "COM10")
io_mod.IO_Read_Map("DS4-Analog Harness.xml")

while not io_mod.IO_Get_Value("lock"):
    continue
sleep(0.05)
result = io_mod.IO_Get_Value("relay1")
print  result
io_mod.IO_Disconnect()
