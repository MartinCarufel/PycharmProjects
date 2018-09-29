#coding:utf-8

import sys
import string
sys.path.append('C:/Drive-W/Internal_tools/Libraries/CANOBDIILibrary/trunk/out')
from CANInterface import CANInterface


log_path = sys.argv[1]

can_device = CANInterface()

baudrate = can_device.Get_BaudRate()
print baudrate

log_to_play = string.replace(log_path, '\\', '/')
print log_to_play
can_device.Play_Log_File(log_to_play)

can_device.CAN_Disconnected()