class Sn_7408:
    """Class defining ... """

    def __init__(self, name):
        self.name = name
        self.pin = [{'no': None, 'name': None, 'type': None, 'state': None},
                    {'no': 1, 'name': '1A', 'type': 'in', 'state': 0},
                    {'no': 2, 'name': '1B', 'type': 'in', 'state': 0},
                    {'no': 3, 'name': '1Y', 'type': 'out', 'state': 0},
                    {'no': 4, 'name': '2A', 'type': 'in', 'state': 0},
                    {'no': 5, 'name': '2B', 'type': 'in', 'state': 0},
                    {'no': 6, 'name': '2Y', 'type': 'out', 'state': 0},
                    {'no': 7, 'name': 'GND', 'type': 'gnd', 'state': 0},
                    {'no': 8, 'name': '3Y', 'type': 'out', 'state': 0},
                    {'no': 9, 'name': '3A', 'type': 'in', 'state': 0},
                    {'no': 10, 'name': '3B', 'type': 'in', 'state': 0},
                    {'no': 11, 'name': '4Y', 'type': 'out', 'state': 0},
                    {'no': 12, 'name': '4A', 'type': 'in', 'state': 0},
                    {'no': 13, 'name': '4B', 'type': 'in', 'state': 0},
                    {'no': 14, 'name': 'VCC', 'type': 'vcc', 'state': 0}]



    def _and(self, a, b):
        if a and b == 1:
            return 1
        else:
            return 0
    def update(self):
        self.pin[3]['state'] = self._and(self.pin[1]['state'], self.pin[2]['state'])
        self.pin[6]['state'] = self._and(self.pin[4]['state'], self.pin[5]['state'])
        self.pin[8]['state'] = self._and(self.pin[9]['state'], self.pin[10]['state'])
        self.pin[11]['state'] = self._and(self.pin[12]['state'], self.pin[13]['state'])
