
class Bus:
    def __init__(self, name, logic_value):
        self.logic_value = logic_value
        self.name = name

        self.pin = [{'no': None, 'name': None, 'type': None, 'state': None},
                    {'no': 1, 'name': self.name, 'type': 'out', 'state': self.logic_value}]


    def set_pin_state(self, pin, state):
        self.pin[pin]['state'] = state

    def get_pin_state(self, pin):
        return self.pin[pin]['state']

    def update(self):
        self.pin[1]['state'] = self.pin[1]['state']