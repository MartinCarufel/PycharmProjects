#coding:utf-8

import tkinter.filedialog
import pandas as pd
import re
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
from sys import argv


def ask_for_new_file():
    while True:
        cont = input("\nDo you want to load a new file (Y/N)")

        if cont.upper() == 'Y':
            return True
        elif cont.upper() == 'N':
            return False
        else:
            print("Please answer by Y or N.")


def create_fig_file_name(path):
    path_list = path.split('/')
    file_name = path_list[-1][:-4]
    return file_name
    print(file_name)

def main():
    load_new_file = True
    lookup_string = "|    490"
    split_pattern = "\| *"
    data = []
    loaded_file_list = []

    try:
        last_data_avg = int(argv[1])
    except IndexError:
        last_data_avg = 25
    while load_new_file:
        path = tkinter.filedialog.askopenfilename()

        loaded_file_list.append(path.split("/")[-1])
        print("Already loaded file: ")
        # print(", ".join(loaded_file_list))
        for i in loaded_file_list:
            print(i)
        with open(path, mode='r') as f:
            for line in f:
                if line.startswith(lookup_string):
                    data.append(int(re.split(split_pattern, line)[4]))
        load_new_file = ask_for_new_file()
        # print(len(data))
        # load_new_file = False

    data_mean = []
    for data_id in range(len(data)):
        if data_id < last_data_avg:
            data_mean.append(np.nan)
        else:
            data_mean.append(mean(data[data_id-last_data_avg:data_id]))

    df = pd.DataFrame(data, columns=["df"])
    df["avg"] = data_mean
    # print(df)
    f = plt.figure()
    f.set_figwidth(15)
    f.set_figheight(6)
    plt.plot(df)
    plt.legend(df)
    plt.subplots_adjust(left=0.05, right=0.99, top=0.95, bottom=0.1)
    plt.ylabel("Nb dropframe")
    plt.xlabel("USB Stress test cycle")
    plt.title("Number of dropframe per USB test cycle")
    plt.grid(axis="y")
    plt.savefig(path + ".pdf", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
