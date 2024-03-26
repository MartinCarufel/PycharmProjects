class Wire:
    def __init__(self, connect):
        self.connect = connect
        self.status = None
        if self.connect[1]['type'] == self.connect[3]['type']:
            self.status = 0
            print('Error wire connect two identical type')
            print('Try to connect {} pin {} as {} to {} pin {} as {}'
                  .format(self.connect[0].name, self.connect[1]['no'], self.connect[1]['type'],
                          self.connect[2].name, self.connect[3]['no'], self.connect[3]['type']))
        else:
            self.status = 1


    def update(self):
        if self.connect[1]['type'] != self.connect[3]['type']:  # compare both pin type are diff
            if self.connect[1]['type'] == 'out':   # if the first pin type is an output
                self.connect[2].set_pin_state(self.connect[3]['no'], self.connect[0].get_pin_state(self.connect[1]['no']))
                # self.connect[3]['state'] = self.connect[1]['state']
                pass
            else:
                self.connect[0].set_pin_state(self.connect[1]['no'], self.connect[2].get_pin_state(self.connect[3]['no']))
                # self.connect[1]['state'] = self.connect[3]['state']


