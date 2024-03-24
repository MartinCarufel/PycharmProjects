#coding:utf-8


import serial

import sys
import os
from time import sleep
from CANInterface import CANInterface
sys.path.append('C:/Drive-W/Internal_tools/Libraries/CANOBDIILibrary/trunk/out/')
from time import sleep

#add comments

can_port = os.environ['ev_can_port']
can = CANInterface()
can.CAN_Connect()
can.CAN_Set_BaudRate(500000, 100000)

ser5 = serial.Serial('COM5',115200)
sleep(.1)
print 'COM5: {} {} {} {}' .format(ser5.baudrate, ser5.bytesize, ser5.parity, ser5.stopbits)
ser5.flushInput()

filtre = b'filter 0 0 0 111\n'

ser5.write(b'filter 0 0 0 111\n\r')
sleep(.2)
can.CAN_Transmit_Message('CAN1', '0x111', '0x10', '0x20', '0x30', '0x40', '0x50', '0x60', '0x70', '0x80')

input('press a key')
ser.flushInput()
buffCount = ser5.inWaiting()
r = ser5.read(buffCount)
ser5.flushInput()
printr
ser5.close()
