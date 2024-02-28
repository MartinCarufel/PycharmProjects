import pyvisa
from time import sleep

class Psu_remote:
    def __init__(self, usb_addr):
        self.usb_add = usb_addr
        self.cmd_del = 0.2
        self.rm = pyvisa.ResourceManager()
        self.spd_add = 'USB0::0xf4ec::0x1430::SPD3XIDC5R1436::INSTR'
        self.SPD = self.rm.open_resource(self.spd_add)
        self.SPD.write_termination = '\n'
        self.SPD.read_termination = '\n'

    def show_connect(self):
        self.SPD.write('*IDN?')
        sleep(self.cmd_del)
        SPDIDN = self.SPD.read()
        print("Power Supply" + str(SPDIDN).rstrip())

    def send_cmd(self, cmd):
        self.SPD.write(cmd)
        sleep(self.cmd_del)

    def read_cmd(self, cmd):
        self.SPD.write(cmd)
        sleep(self.cmd_del)
        return self.SPD.read()

def main():
    rm = Psu_remote('USB0::0xf4ec::0x1430::SPD3XIDC5R1436::INSTR')
    rm.show_connect()
    timer_step = ['timer:set CH1,1,2,3.2,5',
                  'timer:set CH1,2,4,3.2,5',
                  'timer:set CH1,3,6,3.2,5',
                  'timer:set CH1,4,8,3.2,5',
                  'timer:set CH1,5,10,3.2,5']

    # for cmd in timer_step:
    #     rm.send_cmd(cmd)
    rm.send_cmd('CH1:voltage 5')
    pass

if __name__ == '__main__':
    main()

"""
cmd_del = 0.2

rm = pyvisa.ResourceManager()
# addres: USB0::0xvendorID::ProductID::serialNumber::INSTR
spd_add = 'USB0::0xf4ec::0x1430::SPD3XIDC5R1436::INSTR'
SPD = rm.open_resource(spd_add)
SPD.write_termination = '\n'
SPD.read_termination = '\n'
SPD.write('*IDN?')
sleep(cmd_del)
SPDIDN = SPD.read()
print("Power Supply" + str(SPDIDN).rstrip())

SPD.write('CH1:voltage 10')
sleep(cmd_del)
# SPD.write('CH1:voltage 5.3')
SPD.write('CH1:current 1.0')
sleep(cmd_del)
SPD.write('output CH1,ON')
sleep(cmd_del)

send_cmd('CH1:voltage 5')
print(read_cmd('measure:current? CH1'))
"""

