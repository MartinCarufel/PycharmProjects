# coding: utf-8
import threading
from time import sleep
import pin


class Connection:
    """Class defining ... """

    def __init__(self, in_id, out_id):
        """Class constructor"""
        self._in_id = in_id
        self._out_id = out_id
        t = threading.Thread(target=self.update).start()

    # def set(self, key, value):
    #     if value in (0, 1):
    #         self._out_o.set(self._in_o.get(key), value)
    #         # self._pin[key] = value
    #
    # def get(self, key):
    #     return


    def update(self):
        """Method that do something"""
        while True:
            pin.pin[self._out_id] = pin.pin[self._in_id]

