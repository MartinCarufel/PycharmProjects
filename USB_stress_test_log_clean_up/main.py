#coding:utf-8

import tkinter.filedialog


def main():
    data = []
    log_data = False
    path = tkinter.filedialog.askopenfilename()
    f = open(path, mode='r')
    indice = 0
    for line in f:
        if "START STRESS TEST" in line or "Thread started: USBStreamThread" in line:
            log_data = True
        elif "Thread stopped from outside: USBStreamThread" in line:
            log_data = False

        if log_data:
            data.append(line)
        if indice % 100000 == 0:
            print('.', end='')
        indice += 1

    f.close()

    with open(path[:-4] + "_clean" + ".txt", mode='w') as wf:
        indice = 0
        for i in data:
            wf.writelines(i)
            if indice % 1000 == 0:
                print('.', end='')
            indice += 1




if __name__ == "__main__":
    main()
