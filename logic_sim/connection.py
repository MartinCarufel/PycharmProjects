# coding: utf-8
import threading
from time import sleep


class Connection:
    """Class defining ... """

    def __init__(self, input, output, pin):
        """Class constructor"""
        # self._pin = {'in': None, 'out': None}
        self._input = input
        self._output = output
        self._pin = pin
        t = threading.Thread(target=self.update).start()


    def update(self):
        """Method that do something"""
        while True:
            self._output.set(self._pin, self._input)
            # print(self._input)
            sleep(1)

