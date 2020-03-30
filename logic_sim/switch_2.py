# coding: utf-8
import threading
from time import sleep

class Switch:
    """Class defining ... """

    def __init__(self, name=None):
        """Class constructor"""
        self.name = name
        self._pin = {'a1': 0, 'y1': 0}
        self._state = False
        threading.Thread(target=self.update).start()
    # def get_input(self, key):
    #     return self._input[key]

    def set(self, key, value):
        if value in (0, 1):
            self._pin[key] = value

    def get(self, key):
        return self._pin[key]

    def get_state(self):
        return self._state

    def set_state(self, value):
        if value in (0, 1):
            self._state = value

    def update(self):
        while True:
            if self._state:
                self._pin['y1'] = self._pin['a1']
                print(self._pin['y1'])

            else:
                self._pin['y1'] = None
            sleep(1)