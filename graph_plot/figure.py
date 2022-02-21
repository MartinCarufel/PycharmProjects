# coding: utf-8
import matplotlib.pyplot as plt
import random


def main():
    print("Hello world")
    x = [i for i in range(10)]
    ser1 = []
    for ser in range(5):
        temp = []
        for i in range(10):
            temp.append(random.randint(1, 20))
        print(temp)
        ser1.append(temp)

        # ser2 = []
        # for i in range(10):
        #     ser2.append(random.randint(1, 20))
        #
        # ser3 = []
        # for i in range(10):
        #     ser3.append(random.randint(1, 20))
    print(ser1)
    for i in ser1:
        plt.plot(x, i)

    # plt.plot([1,2,3,4,5], [1,2,3,4,10])
    # plt.show()

    # fig, (ax1) = plt.subplots(1, 1,figsize=(6, 6))
    # ax1.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 10], 'go')
    # plt.tight_layout()
    plt.show()




if __name__ == '__main__':
    main()
