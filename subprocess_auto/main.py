# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import subprocess


def main():
    # Use a breakpoint in the code line below to debug your script.
    for i in range(3):
        p = subprocess.Popen("D:/tools/vivo-usb-test 5.2.0-1633/usb_stress_test.exe", cwd='D:/tools/vivo-usb-test 5.2.0-1633/')
        p.wait()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
