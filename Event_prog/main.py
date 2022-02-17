# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
Event prog:


"""

from threading import Thread
import random
from time import sleep

class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

class Publisher:
    def __init__(self, events):
        self.subscribers = {event:dict() for event in events}
    def get_subscribers(self, event):
        return self.subscribers[event]
    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, "update")
        self.get_subscribers(event)[who] = callback
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


class Pige:
    def __init__(self):
        self.pige = 0
    def nouvelle(self):
        sleep(3)
        self.pige = random.randint(0, 10)
        print(self.pige)

def check_num():
    while True:
        sleep(.5)
        if p.pige == random.randint(0, 10):
            pub.dispatch("gagne", "Tu as gangné le nombre était {}".format(p.pige))
        else:
            print("echec")

def draw_number():
    sleep(5)
    draw = random.randint(0, 10)
    return draw

def new_draw():
    while True:
        p.nouvelle()
        sleep(5)

pub = Publisher(["gagne"])
p = Pige()
p.nouvelle()
gagne = Subscriber("toto")
pub.register("gagne", gagne)

tr = Thread(target=check_num)
tr2 = Thread(target=new_draw)
tr.start()
tr2.start()
