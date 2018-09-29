#coding:utf-8

import sys
import string
sys.path.append('C:/Drive-W/Internal_tools/Libraries/CANOBDIILibrary/trunk/out')
sys.path.append('C:/Drive-W/Internal_tools/Libraries/FlashNVFS/trunk/out')
from NvfsInterface import NvfsInterface as nvfs
from CANInterface import CANInterface


#data = nvfs.nvfs_get_all_variables()
#print data

can1_speed = 500000
can2_speed = 100000
#log_path = r"C:\Drive-W\Project\hk13\testbench\trunk\digital\CAN\Log\2018_Sedona_Key\20171213-100439\0101-front_driver_door.csv"

log_path = sys.argv[1]

can_device = CANInterface()

baudrate = can_device.Get_BaudRate()
print baudrate
can_device.Set_BaudRate(can1_speed, can2_speed)
baudrate = can_device.Get_BaudRate()
print baudrate

log_to_play = string.replace(log_path, '\\', '/')
print log_to_play
can_device.Play_Log_File(log_to_play)

can_device.CAN_Disconnected()