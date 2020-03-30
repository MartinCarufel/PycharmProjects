# coding: utf-8
import threading
from time import sleep

class Switch:
    """Class defining ... """

    def __init__(self, name=None):
        """Class constructor"""
        self.name = name
        self._pin = {'in': None, 'out': None}
        self._state = False

        t = threading.Thread(target=self.update).start()
        # globals()[name + '_out'] = 0

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
            self._pin['out'] = self._pin['in']
            # if self._state:
            #     # print('sw update, SW1 on')
            #     # print(self._pin['in'])
            #     self._pin['out'] = self._pin['in']
            # else:
            #     self._pin['out'] = None
            # sleep(1)

    def set_state(self, state):
        """Method that do something"""
        self._state = state
        # globals()[self.name + '_out'] = state

