# coding=UTF-8

import enum

class Status(enum.Enum):
    off = 0
    standby = 1
    sleep = 2
    on = 3

    @staticmethod
    def list_name():
        return list(map(lambda c: c.name, Status))


    @staticmethod
    def list_value():
        return list(map(lambda c: c.value, Status))


    @staticmethod
    def dic_value_name():
        result = {}
        name = list(map(lambda c: c.name, Status))
        value = list(map(lambda c: c.value, Status))
        for i in zip(name, value):
            # print(i)
            result.update({i[0]: i[1]})
        return result



def status_name_from_id():
    current_state = 0
    for i in range(4):
        print('Current State: {}'.format(Status(current_state).name))
        current_state += 1

def status_id_from_name():
    print(Status.list_name())
    print(Status.list_value())



def main():
    # status_id_from_name()
    print(Status.dic_value_name())



if __name__ == '__main__':
    main()
