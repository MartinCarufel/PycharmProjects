#coding:utf-8

import tkinter.filedialog
from time import sleep
from os import system


def main():
    data = []
    log_data = False
    path = tkinter.filedialog.askopenfilename()
    f = open(path, mode='r')
    indice = 0
    progress = []
    for line in f:
        if "START STRESS TEST" in line or "Thread started: USBStreamThread" in line:
            log_data = True
        elif "Thread stopped from outside: USBStreamThread" in line:
            log_data = False

        if log_data:
            data.append(line)

        if (indice % 50000) == 0:
            progress.append(".")
            _ = system('cls')
            print("".join(progress))
        indice += 1

    with open(path[:-4] + "_clean" + ".txt", mode='w') as wf:
        progress = []
        indice = 0
        for i in data:
            wf.writelines(i)
            if (indice % 5000) == 0:
                progress.append(".")
                _ = system('cls')
                print("".join(progress))

            indice += 1
    filename = path[:-4] + "_clean" + ".txt"
    print("File created: ", filename)


if __name__ == "__main__":
    main()
