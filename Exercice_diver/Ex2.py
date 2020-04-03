# coding=UTF-8


class MyEnum:
    off, on, sleep, standby, reset = range(5)


def main():
    # print(MyEnum.sleep)
    MyEnum.__dict__
    if MyEnum.sleep % 2 == 0:
        print('yes')
    pass


if __name__ == '__main__':
    main()