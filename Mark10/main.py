# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial
from time import sleep


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    s = serial.Serial("COM3", 115200)
    sleep(0.1)
    if (s.is_open):
        print("Connection established")

    while True:
        s.write(b'?\r\n')
        sleep(0.05)

        if s.in_waiting > 6:
            # print("data in")
            # sleep(0.01)
            try:
                print("Force: {}                  ".format(float(s.readline())), end="\r")   # remove \r\n
            except ValueError:
                print("Force: {}".format(str(s.readline().decode('utf-8'))), end="\r")  # remove \r\n
            sleep(0.05)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
