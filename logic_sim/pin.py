class Pin:

    # __init__ function
    def __init__(self):
        self.pin = {}
        # Function to add key:value
    staticmethod
    def add(self, key, value):
        self.pin[key] = value

    def change(self, key, value):
        if key in self.pin:
            self.pin[key] = value
        else:
            print('{} no data found'.format(key))