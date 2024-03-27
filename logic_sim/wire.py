class Wire:
    def __init__(self, name, connect):
        """
        Connect: list of device object , pin to device object to pin
        """
        self.connect = connect
        self.status = None
        self.name = name
        if self.connect[0].pin[self.connect[1]]['type'] == self.connect[2].pin[self.connect[3]]['type']:
        # if self.connect[1]['type'] == self.connect[3]['type']:
            self.status = 0
            print('Error wire connect two identical type')
                  # print('Try to connect {} pin {} as {} to {} pin {} as {}'
               #    .format(self.connect[0].name, self.connect[1]['no'], self.connect[1]['type'],
               #            self.connect[2].name, self.connect[3]['no'], self.connect[3]['type']))"""
            print('Try to connect {} pin {} as {} to {} pin {} as {}'
              .format(self.connect[0].name, self.connect[1], self.connect[0].pin[self.connect[1]]['type'],
                      self.connect[2].name, self.connect[3], self.connect[2].pin[self.connect[3]]['type']))
        else:
            self.status = 1


    def update2(self):
        if self.connect[1]['type'] != self.connect[3]['type']:  # compare both pin type are diff
            if self.connect[1]['type'] == 'out':   # if the first pin type is an output
                self.connect[2].set_pin_state(self.connect[3]['no'], self.connect[0].get_pin_state(self.connect[1]['no']))
                # self.connect[3]['state'] = self.connect[1]['state']
                pass
            else:
                self.connect[0].set_pin_state(self.connect[1]['no'], self.connect[2].get_pin_state(self.connect[3]['no']))
                # self.connect[1]['state'] = self.connect[3]['state']

    def update(self):
        if self.connect[0].pin[self.connect[1]]['type'] != self.connect[2].pin[self.connect[3]]['type']:  # compare both pin type are diff
            if self.connect[0].pin[self.connect[1]]['type'] == 'out':   # if the first pin type is an output
                self.connect[2].set_pin_state(self.connect[3], self.connect[0].get_pin_state(self.connect[1]))
                # self.connect[3]['state'] = self.connect[1]['state']
                pass
            else:
                self.connect[0].set_pin_state(self.connect[1], self.connect[2].get_pin_state(self.connect[3]))
                # self.connect[1]['state'] = self.connect[3]['state']
