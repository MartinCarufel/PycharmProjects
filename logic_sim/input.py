# coding: utf-8
import pin
class Input:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""
        self.name = name
        pin.pin.update({self.name+'out': 0})

    def set(self, key, value):
        if value in (0, 1):
            pin.pin[self.name+key] = value

    def get(self, key):
        return pin.pin[self.name+key]
