# coding: utf-8
import pin
import threading

class TTL_7408:
    """Class defining ... """

    def __init__(self, name=None):
        """Class constructor"""
        self.name = name
        self._pin = {'a1': 0, 'b1': 0, 'a2': 0, 'b2': 0, 'a3': 0, 'b3': 0, 'a4': 0, 'b4': 0, 'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0}
        threading.Thread(target=self.update).start()
    # def get_input(self, key):
    #     return self._input[key]

    def set(self, key, value):
        if value in (0, 1):
            self._pin[key] = value

    def get(self, key):
        return self._pin[key]

    def update(self):
        while True:
            self._pin['y1'] = int(self._pin['a1']) & int(self._pin['b1'])
            self._pin['y2'] = int(self._pin['a2']) & int(self._pin['b2'])
            self._pin['y3'] = int(self._pin['a3']) & int(self._pin['b3'])
            self._pin['y4'] = int(self._pin['a4']) & int(self._pin['b4'])
