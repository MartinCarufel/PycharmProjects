# coding: utf-8
import threading
from time import sleep

class Switch:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""
        self.name = name
        self._pin = {'in':None, 'out':None}
        self._state = False
        t = threading.Thread(target=self.update).start()
        # globals()[name + '_out'] = 0

    def __setitem__(self, pin, value):
        if value in (0, 1):
            self._pin[pin] = value

    def __getitem__(self, pin):
        return self._pin[pin]

    def update(self):
        while True:
            if self._state:
                # print('sw update, SW1 on')
                self._pin['out'] = self._pin['in']
            else:
                self._pin['out'] = None
            # sleep(1)

    def set_state(self, state):
        """Method that do something"""
        self._state = state
        # globals()[self.name + '_out'] = state

