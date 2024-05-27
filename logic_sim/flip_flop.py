class Sn74ls279a:

    def __init__(self, name):
        self.name = name
        self.state = 0

        self.pin = [{'no': None, 'name': None, 'type': None, 'state': None},
                {'no': 1, 'name': '1R', 'type': 'in', 'state': 0},
                {'no': 2, 'name': '1S1', 'type': 'in', 'state': 0},
                {'no': 3, 'name': '1S2', 'type': 'in', 'state': 0},
                {'no': 4, 'name': '1Q', 'type': 'out', 'state': 0, 'prev_state': 0},
                {'no': 5, 'name': '2R', 'type': 'in', 'state': 0},
                {'no': 6, 'name': '2S', 'type': 'in', 'state': 0},
                {'no': 7, 'name': '2Q', 'type': 'out', 'state': 0, 'prev_state': 0},
                {'no': 8, 'name': 'GND', 'type': 'gnd', 'state': 0},
                {'no': 9, 'name': '3Q', 'type': 'out', 'state': 0, 'prev_state': 0},
                {'no': 10, 'name': '3R', 'type': 'in', 'state': 0},
                {'no': 11, 'name': '3S1', 'type': 'in', 'state': 0},
                {'no': 12, 'name': '3S2', 'type': 'in', 'state': 0},
                {'no': 13, 'name': '4Q', 'type': 'out', 'state': 0, 'prev_state': 0},
                {'no': 14, 'name': '4R', 'type': 'in', 'state': 0},
                {'no': 15, 'name': '4S', 'type': 'in', 'state': 0},
                {'no': 16, 'name': 'VCC', 'type': 'vcc', 'state': 0}]

    def set_pin_state(self, pin, state):
        self.pin[pin]['state'] = state

    def get_pin_state(self, pin):
        return self.pin[pin]['state']

    def update(self):
        self.pin[4]['state'] = self._flip_flop(self.pin[2]['state'], self.pin[3]['state'], self.pin[1]['state'],
                                               self.pin[4])
        self.pin[7]['state'] = self._flip_flop(self.pin[6]['state'], self.pin[6]['state'], self.pin[5]['state'],
                                               self.pin[7])
        self.pin[9]['state'] = self._flip_flop(self.pin[11]['state'], self.pin[12]['state'], self.pin[10]['state'],
                                               self.pin[9])
        self.pin[13]['state'] = self._flip_flop(self.pin[15]['state'], self.pin[15]['state'], self.pin[14]['state'],
                                               self.pin[13])


    def _flip_flop(self, s1, s2, r, out_pin):
        if s1 == 0 and s2 == 0 and r == 1:
            out_pin['prev_state'] = 1
            return 1
        if s1 == 1 and s2 == 1 and r == 0:
            out_pin['prev_state'] = 0
            return 0
        if s1 == 1 and s2 == 1 and r == 1:
            return out_pin['prev_state']




