class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{} got message {}".format(self.name, message))

    def test1(self):
        print("Salut")


class Publisher:
    def __init__(self, events):
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback=getattr(who, "update")
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)

    def dispatch2(self, event):
        for subscriber, callback in self.get_subscribers(event).items():
            callback()

pub = Publisher(["lunch", "dinner", "test"])
bob = Subscriber("bob")
alice = Subscriber("Alice")
john = Subscriber("John")

pub.register("lunch", bob)
pub.register("dinner", alice)
pub.register("lunch", john)
pub.register("dinner", john)
pub.register("test", bob, callback=bob.test1)

pub.dispatch("lunch", "hello")
pub.dispatch2("test")
# input("press a key")
