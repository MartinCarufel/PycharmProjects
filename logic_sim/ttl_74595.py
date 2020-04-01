# coding: utf-8
import pin
import threading
from time import sleep

class TTL_7408:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""
        self.name = name
        # self._pin = {'a1': 0, 'b1': 0, 'a2': 0, 'b2': 0, 'a3': 0, 'b3': 0, 'a4': 0, 'b4': 0, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0}
        pin.pin.update({self.name + 'oe': 0, self.name + 'rclk': 0, self.name + 'srclr': 0, self.name + 'srclk': 0, self.name + 'ser': 0,
                        self.name + 'qa': 0, self.name + 'qb': 0, self.name + 'qc': 0, self.name + 'qd': 0, self.name + 'qe': 0,
                        self.name + 'qf': 0, self.name + 'qg': 0, self.name + 'qh': 0, self.name + 'qhi': 0})
        self.shift_register = 0b0
        self.storage_register = 0b0
        self.srclk = 0
        self.rclk = 0


        threading.Thread(target=self.update).start()
    # def get_input(self, key):
    #     return self._input[key]

    def set(self, key, value):
        if value in (0, 1):
            pin.pin[self.name + key] = value

    def get(self, key):
        return pin.pin[self.name + key]

    def update(self):
        while True:
            if pin.pin[self.name + 'srclr']:
                self.shift_register = 0
            if pin.pin[self.name + 'srclk'] == 1 and self.srclk == 0:
                sleep(0.005)
                self.shift_register = (self.shift_register << 1) + pin.pin[self.name + 'ser']
                if (self.shift_register & 0x100) == 0x100:
                    print('shift register overflow')
                    pin.pin[self.name + 'qhi'] = 1
                self.shift_register = self.shift_register & 0xff

            if pin.pin(self.name['rclk']) == 1 and self.storage_register ==0:
                self.storage_register = self.shift_register

            if pin.pin[self.name + 'oe'] == 0:
                pin.pin[self.name + 'qa'] = int(bool(self.storage_register & 0x01))
                pin.pin[self.name + 'qb'] = int(bool(self.storage_register & 0x02))
                pin.pin[self.name + 'qc'] = int(bool(self.storage_register & 0x04))
                pin.pin[self.name + 'qd'] = int(bool(self.storage_register & 0x08))
                pin.pin[self.name + 'qe'] = int(bool(self.storage_register & 0x10))
                pin.pin[self.name + 'qf'] = int(bool(self.storage_register & 0x20))
                pin.pin[self.name + 'qg'] = int(bool(self.storage_register & 0x40))
                pin.pin[self.name + 'qh'] = int(bool(self.storage_register & 0x80))

            self.srclk = pin.pin[self.name + 'srclk']
            self.rclk = pin.pin[self.name + 'rclk']

            