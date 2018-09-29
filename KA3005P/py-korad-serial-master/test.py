import serial
from time import sleep
from koradserial import KoradSerial
from koradserial import OnOffState
from koradserial import Tracking


mydevice = KoradSerial("COM3",1)
channel = mydevice.channels[0]
channel.voltage = 5
channel.current = 2
mydevice.output.off()
#power_state = mydevice.status
print(OnOffState.on.value)


load = channel.output_current
print(load)

# #wait = input("press to continue" )
# wait = 'r'
# while wait == 'r':
#     wait = input("press to continue: ")
#     load = channel.output_current
#     print(load)

wait = input("press to continue: ")
mydevice.output.off()
mydevice.close()





# ser = serial.Serial('COM3')
# print(ser.name)
# #ser.write(b'VSET1:6.34')
# #ser.write(b'OUT1')
# text = 'VSET1:10.34'
# ser.write(text.encode('ascii'))
# sleep(0.1)
#
# text = 'OUT0'
# ser.write(text.encode('ascii'))


