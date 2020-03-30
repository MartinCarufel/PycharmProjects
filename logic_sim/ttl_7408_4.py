# coding: utf-8
import threading
from time import sleep

class TTL_7408:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""

        self.name = name
        self._a1 = 0
        self._b1 = 0
        self._a2 = 0
        self._b2 = 0
        self._a3 = 0
        self._b3 = 0
        self._a4 = 0
        self._b4 = 0
        self._y1 = 0
        self._y2 = 0
        self._y3 = 0
        self._y4 = 0
        self.linput = {'a1': self._a1}
        threading.Thread(target=self.update).start()

    def __get_a1(self):
        return self._a1

    def __set_a1(self, value):
        if value in (0, 1):
            self._a1 = value

    def __get_b1(self):
        return self._b1

    def __set_b1(self, value):
        if value in (0, 1):
            self._b1 = value

    def __get_a2(self):
        return self._a2

    def __set_a2(self, value):
        if value in (0, 1):
            self._a2 = value

    def __get_b2(self):
        return self._b2

    def __set_b2(self, value):
        if value in (0, 1):
            self._b2 = value

    def __get_a3(self):
        return self._a3

    def __set_a3(self, value):
        if value in (0, 1):
            self._a3 = value

    def __get_b3(self):
        return self._a3

    def __set_b3(self, value):
        if value in (0, 1):
            self._b3 = value

    def __get_a4(self):
        return self._a4

    def __set_a4(self, value):
        if value in (0, 1):
            self._a4 = value

    def __get_b4(self):
        return self._b4

    def __set_b4(self, value):
        if value in (0, 1):
            self._b4 = value

    def __get_y1(self):
        return self._y1

    def __set_y1(self, value):
        self._y1 = value

    def __get_y2(self):
        return self._y2

    def __set_y2(self, value):
        self._y2 = value

    def __get_y3(self):
        return self._y3

    def __set_y3(self, value):
        self._y3 = value

    def __get_y4(self):
        return self._y4

    def __set_y4(self, value):
        self._y4 = value

    a1 = property(__get_a1, __set_a1)
    b1 = property(__get_b1, __set_b1)
    a2 = property(__get_a2, __set_a2)
    b2 = property(__get_b2, __set_b2)
    a3 = property(__get_a3, __set_a3)
    b3 = property(__get_b3, __set_b3)
    a4 = property(__get_a4, __set_a4)
    b4 = property(__get_b4, __set_b4)
    y1 = property(__get_y1, __set_y1)
    y2 = property(__get_y2, __set_y2)
    y3 = property(__get_y3, __set_y3)
    y4 = property(__get_y4, __set_y4)

    def update(self):
        while True:
            self._y1 = int(self._a1) & int(self._b1)
            self._y2 = int(self._a2) & int(self._b2)
            self._y3 = int(self._a3) & int(self._b3)
            self._y4 = int(self._a4) & int(self._b4)

    def xx(self, input, value):
        print('asd')
        # self.linput['input'] = value
        print(self.linput[input])
        self._a1 = value
        sleep(1)
        print(self.linput[input])