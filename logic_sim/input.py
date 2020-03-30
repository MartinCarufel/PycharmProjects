# coding: utf-8

class Input:
    """Class defining ... """

    def __init__(self, name=None):
        """Class constructor"""
        self._pin = {'out': None}
        self.input_name = name

    def set(self, key, value):
        if value in (0, 1):
            self._pin[key] = value

    def get(self, key):
        return self._pin[key]
