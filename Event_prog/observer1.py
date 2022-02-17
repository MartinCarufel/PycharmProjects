# coding: utf-8
class subscriber:
    def __init__(self, name):
        self.name = name
    def recieve(self, message):
        print(message)

class Publisher:
    def __init__(self):
        self.subscriber = dict()
    def register(self, who, callback = None):
        if callback is None:
            callback = getattr(who, "update")
        self.subscriber.add(who)


pub = Publisher()
bob = subscriber("bob")