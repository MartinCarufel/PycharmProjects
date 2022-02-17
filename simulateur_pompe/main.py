from threading import Thread
from time import sleep


class Tank(object):
    def __init__(self, name, capacity, current_volume=0, low_alarm=10, high_alarm=90):
        self.name = name
        self.capacity = capacity  # Max tank capacity
        self.low_alarm = low_alarm
        self.low_indicator = False
        self.high_alarm = high_alarm
        self.high_indicator = False
        self.current_volume = current_volume
        if self.current_volume <= self.low_alarm:
            self._low_alarm()
        elif self.current_volume >= self.high_alarm:
            self._high_alarm()
        else:
            self._clear_alarm()

    def fill(self, volume):
        self.current_volume += volume
        self.current_volume = min(self.capacity, self.current_volume)
        if self.current_volume >= self.high_alarm:
            self._high_alarm()
        if self.current_volume <= self.low_alarm:
            self._low_alarm()

    def drain(self, volume):
        if self.current_volume > 0:
            self.current_volume -= volume
            self.current_volume = max(0, self.current_volume)
        if self.current_volume <= self.low_alarm:
            self._low_alarm()
        if self.current_volume >= self.high_alarm:
            self._high_alarm()

    def _low_alarm(self):
        self.low_alarm = True
        print("Tank level is low")

    def _high_alarm(self):
        self.high_alarm = True
        print("Tank level is high")

    def _clear_alarm(self):
        self.low_alarm = False
        self.low_alarm = False
        print("Tank level is OK")


class Pump(object):
    def __init__(self, function, flow_rate):
        self.flow_rate = flow_rate  # In Liter per second
        self.function = function
        self.enable_state = None
        self.pumping = Thread(target=self.pump_activate)
        self.pumping.start()

    def pump_activate(self):
        while True:
            if self.enable_state:
                self.function(self.flow_rate)
            sleep(1)

    def pump_enable(self):
        self.enable_state = True
        print("Start pumping")

    def pump_disable(self):
        self.enable_state = False
        print("Stop pumping")


tank1 = Tank('Tank 1', 100)
pump1 = Pump(tank1.fill, 13)
pump1.pump_enable()
pump2 = Pump(tank1.drain, 17)
# pump2.pump_enable()
while True:
    print(tank1.current_volume)
    sleep(0.3)
# pump1.pump_disable()
# pump2.pump_enable()

# while tank1.current_volume < 95:
#     tank1.fill(5)
#     print("{} current volume is {}".format(tank1.name, tank1.current_volume))
#     sleep(0.4)
