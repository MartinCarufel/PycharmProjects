# coding: utf-8
import threading

class TTL_7408:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""
        self.name = name

        self._input = {'a1': 0, 'b1': 0, 'a2': 0, 'b2': 0, 'a3': 0, 'b3': 0, 'a4': 0, 'b4': 0}
        self._gate_out = {'y1': 0, 'y2': 0, 'y3': 0, 'y4': 0}
        t = threading.Thread(target=self.update).start()

    def __setitem__(self, pin, value):
        if value in (0, 1):
            self._input[pin] = value

    def __getitem__(self, pin):
        return self._gate_out[pin]


    def update(self):
        while True:
            self._gate_out['y1'] = int(self._input['a1']) & int(self._input['b1'])
            self._gate_out['y2'] = int(self._input['a2']) & int(self._input['b2'])
            self._gate_out['y3'] = int(self._input['a3']) & int(self._input['b3'])
            self._gate_out['y4'] = int(self._input['a4']) & int(self._input['b4'])

