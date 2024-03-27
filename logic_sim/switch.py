# coding: utf-8
from threading import Thread
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
        # print(f'Switch pos = {self._position}')

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

class Push_SPNO:
    def __init__(self, name, pull):
        self.name = name
        self.active = 0
        self.pull = pull.lower()
        if self.pull not in ['up', 'down']:
            raise Exception('Error pull type should be up or down')
        else:
            if pull == 'up':
                self.default_state = 1
            else:
                self.default_state = 0
        self.pin = [{'no': None, 'name': None, 'type': None, 'state': None},
                    {'no': 1, 'name': '1', 'type': 'in', 'state': 0},
                    {'no': 2, 'name': '2', 'type': 'out', 'state': self.default_state}]


    def set_pin_state(self, pin, state):
        self.pin[pin]['state'] = state

    def get_pin_state(self, pin):
        return self.pin[pin]['state']

    def activate(self, time_ms):
        self.push_time_s = time_ms/1000
        t1 = Thread(target=self._push_timer, args=([self.push_time_s]))
        t1.start()

    def _push_timer(self, push_time_s):
        self.active = 1
        # update
        self.update()
        sleep(push_time_s)
        # update
        self.update()
        self.active = 0



    def update(self):
        if self.active == 1:
            self.pin[2]['state'] = self.pin[1]['state']
        else:
            self.pin[2]['state'] = self.default_state
