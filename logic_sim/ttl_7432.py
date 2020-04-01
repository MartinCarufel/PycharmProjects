# coding: utf-8
import pin
import threading

class TTL_7432:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""
        self.name = name
        # self._pin = {'a1': 0, 'b1': 0, 'a2': 0, 'b2': 0, 'a3': 0, 'b3': 0, 'a4': 0, 'b4': 0, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0}
        pin.pin.update({self.name+'a1': 0, self.name+'b1': 0, self.name+'a2': 0, self.name+'b2': 0, self.name+'a3': 0,
                        self.name+'b3': 0, self.name+'a4': 0, self.name+'b4': 0, self.name+'y1': 0, self.name+'y2': 0,
                        self.name+'y3': 0, self.name+'y4': 0})
        threading.Thread(target=self.update).start()
    # def get_input(self, key):
    #     return self._input[key]

    def set(self, key, value):
        if value in (0, 1):
            pin.pin[self.name+key] = value

    def get(self, key):
        return pin.pin[self.name+key]

    def update(self):
        while True:
            try:
                pin.pin[self.name+'y1'] = int(pin.pin[self.name+'a1']) | int(pin.pin[self.name+'b1'])
            except TypeError:
                pin.pin[self.name + 'y1'] = 0

            try:
                pin.pin[self.name+'y2'] = int(pin.pin[self.name+'a2']) | int(pin.pin[self.name+'b2'])
            except TypeError:
                pin.pin[self.name + 'y2'] = 0

            try:
                pin.pin[self.name+'y3'] = int(pin.pin[self.name+'a3']) | int(pin.pin[self.name+'b3'])
            except TypeError:
                pin.pin[self.name + 'y3'] = 0

            try:
                pin.pin[self.name+'y4'] = int(pin.pin[self.name+'a4']) | int(pin.pin[self.name+'b4'])
            except TypeError:
                pin.pin[self.name + 'y4'] = 0
