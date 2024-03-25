
class Sn_7404:
    """Class defining ... """

    def __init__(self, name):
        self.name = name
        self.pin = [{'no': None, 'name': None, 'type': None, 'state': None},
                    {'no': 1, 'name': '1A', 'type': 'in', 'state': 0},
                    {'no': 2, 'name': '2Y', 'type': 'out', 'state': 0},
                    {'no': 3, 'name': '2A', 'type': 'in', 'state': 0},
                    {'no': 4, 'name': '2Y', 'type': 'out', 'state': 0},
                    {'no': 5, 'name': '3A', 'type': 'in', 'state': 0},
                    {'no': 6, 'name': '3Y', 'type': 'out', 'state': 0},
                    {'no': 7, 'name': 'GND', 'type': 'gnd', 'state': 0},
                    {'no': 8, 'name': '4Y', 'type': 'out', 'state': 0},
                    {'no': 9, 'name': '4A', 'type': 'in', 'state': 0},
                    {'no': 10, 'name': '5Y', 'type': 'out', 'state': 0},
                    {'no': 11, 'name': '5A', 'type': 'in', 'state': 0},
                    {'no': 12, 'name': '6Y', 'type': 'out', 'state': 0},
                    {'no': 13, 'name': '6A', 'type': 'in', 'state': 0},
                    {'no': 14, 'name': 'VCC', 'type': 'vcc', 'state': 0}]

        self.output_pin = [out['no'] for out in self.pin if out['type'] == 'out']

    def _invert(self, value):
        if value == 0:
            return 1
        else:
            return 0
    def update(self):
        self.pin[2]['state'] = self._invert(self.pin[1]['state'])
        self.pin[4]['state'] = self._invert(self.pin[3]['state'])
        self.pin[6]['state'] = self._invert(self.pin[5]['state'])
        self.pin[8]['state'] = self._invert(self.pin[9]['state'])
        self.pin[10]['state'] = self._invert(self.pin[11]['state'])
        self.pin[12]['state'] = self._invert(self.pin[13]['state'])
