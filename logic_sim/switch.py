# coding: utf-8
import threading
import pin
from time import sleep


class Switch_SPDT:
    """2 possibles position, int: 1 or 2
    Define in list the pin type

    example pin 1 as in pin 2 as out pin 3 as in
    ['in', 'out', 'in']"""
    def __init__(self, name, pin_type, position=1):
        self.name = name
        self.pin_type = [x.lower() for x in pin_type]
        for pin in self.pin_type:
            if pin not in['in', 'out']:
                raise Exception('Error pin type should be in or out')
        self._position = position
        self.pin = [{'no': None, 'name': None, 'type': None, 'state': None},
                    {'no': 1, 'name': '1', 'type': self.pin_type[0], 'state': 0},
                    {'no': 2, 'name': '2', 'type': self.pin_type[1], 'state': 0},
                    {'no': 3, 'name': '3', 'type': self.pin_type[2], 'state': 0}]

    def set_pin_state(self, pin, state):
        self.pin[pin]['state'] = state

    def get_pin_state(self, pin):
        return self.pin[pin]['state']

    def switch_pos(self, position):
        try:
            if position not in [1, 2]:
                raise Exception("Wrong position mode")
            self._position = position
        except Exception as e:
            print(e)
            pass
        print(f'Switch pos = {self._position}')

    def update(self):
        if self._position == 1:
            if self.pin[2]['type'] == 'out':
                self.pin[2]['state'] = self.pin[1]['state']
            else:
                self.pin[1]['state'] = self.pin[2]['state']
        if self._position == 2:
            if self.pin[2]['type'] == 'out':
                self.pin[2]['state'] = self.pin[3]['state']
            else:
                self.pin[3]['state'] = self.pin[2]['state']

class Switch2:
    """Class defining ... """

    def __init__(self, name):
        """Class constructor"""
        self.name = name
        pin.pin.update({self.name+'a1':0, self.name+'y1':0})
        self._state = False
        threading.Thread(target=self.update).start()
    # def get_input(self, key):
    #     return self._input[key]

    def set(self, key, value):
        if value in (0, 1):
            pin.pin[self.name+key] = value

    def get(self, key):
        return pin.pin[self.name+key]

    def get_state(self):
        return self._state

    def set_state(self, value):
        if value in (0, 1):
            self._state = value

    def update(self):
        while True:
            if self._state:
                pin.pin[self.name+'y1'] = pin.pin[self.name+'a1']
                # print(self._pin['y1'])

            else:
                pin.pin[self.name+'y1'] = None
