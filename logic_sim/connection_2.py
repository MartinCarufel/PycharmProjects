# coding: utf-8
import threading
from time import sleep


class Connection:
    """Class defining ... """

    def __init__(self, input, output, pin):
        """Class constructor"""
        self._pin = {'in': input, 'out': output, 'pin': pin}
        # self._input = input
        # self._output = output
        # self._pin = pin
        t = threading.Thread(target=self.update).start()

    def set(self, key, value):
        if value in (0, 1):
            self._pin[key] = value

    def get(self, key):
        return self._pin[key]


    def update(self):
        """Method that do something"""
        while True:

            self._pin['out'].set(self._pin['pin'], self._pin['in'])
            # print(self._input)
            sleep(1)

