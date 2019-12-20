#coding:utf-8
import sys
sys.path.append('C:/Drive-W/Internal_tools/Libraries/CANOBDIILibrary/trunk/out/')
from CANInterface import CANInterface

can = CANInterface()
can.CAN_Connect()
baud_rate = can.CAN_Get_BaudRate()
print baud_rate

can.CAN_Broadcast_Message(10, 10, 'CAN1', '0x101', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08')
can.CAN_Disconnect()