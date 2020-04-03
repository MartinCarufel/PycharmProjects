# coding= UTF-8

import threading
import queue
from time import sleep


class Value_Store():
    def __init__(self):
        self.value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value



class My_Thread(threading.Thread):

    def __init__(self, wait_time, message, q):
        self.__wait_time = wait_time
        self.__message = message
        self.stop_event = threading.Event()
        self.q = q
        self.cycle = 0
        threading.Thread.__init__(self)

    @property
    def wait_time(self):
        return self.__wait_time

    @wait_time.setter
    def wait_time(self, wait_time):
        self.__wait_time = wait_time


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message





    def run(self):
        print('run')
        print(self.stop_event.is_set())
        while not self.stop_event.is_set():
            self.cycle += 1
            # self.q.set_value(self.cycle)
            self.q.value = self.cycle
            print('Thread say: %s, on cycle: %s' %(self.message, self.cycle))
            sleep(self.wait_time)


    def join(self):
        self.stop_event.set()
        threading.Thread.join(self)


def main():
    q = Value_Store()
    t1 = My_Thread(.5, 'bonjour', q)
    t1.start()
    for i in range(3):
        sleep(3)
        print(q.value)
    t1.join()


if __name__ == '__main__':
    main()