import serial
from time import sleep
from koradserial import KoradSerial
from koradserial import OnOffState
from koradserial import Tracking


mydevice = KoradSerial("COM3",False)
channel = mydevice.channels[0]

channel.voltage = 12

dev_status = mydevice.status
print(dev_status)
mydevice.output.on()
dev_status = mydevice.status
print(dev_status)
load = {}

# for i in range(50, 150, 5):
#     channel.voltage = i/10
#     sleep(0.01)
#     #load.append(channel.output_current)
#     load["{} volt".format(i/10)] = "{} Amp".format(channel.output_current)
#
# for i in range(150, 45, -5):
#     channel.voltage = i / 10
#     sleep(0.01)
#     #load.append(channel.output_current)
#     load["{} volt".format(i)] = "{} Amp".format(channel.output_current)



#mydevice.output.off()
#print(load)


#channel.voltage = 15
#channel.current = 2
#mydevice.output.on()

#load = channel.output_current
#print(load)

# #wait = input("press to continue" )
# wait = 'r'
# while wait == 'r':
#     wait = input("press to continue: ")
#     load = channel.output_current
#     print(load)

#wait = input("press to continue: ")
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


