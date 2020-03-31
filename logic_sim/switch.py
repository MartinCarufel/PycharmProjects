# coding: utf-8
import threading
import pin
from time import sleep

class Switch:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""
        self.name = name
        pin.pin.update({self.name+'a1':0, self.name+'y1':0})
        self._state = False
        threading.Thread(target=self.update).start()
    # def get_input(self, key):
    #     return self._input[key]

    def set(self, key, value):
        if value in (0, 1):
            pin.pin[self.name+key] = value

    def get(self, key):
        return pin.pin[self.name+key]

    def get_state(self):
        return self._state

    def set_state(self, value):
        if value in (0, 1):
            self._state = value

    def update(self):
        while True:
            if self._state:
                pin.pin[self.name+'y1'] = pin.pin[self.name+'a1']
                # print(self._pin['y1'])

            else:
                pin.pin[self.name+'y1'] = None
