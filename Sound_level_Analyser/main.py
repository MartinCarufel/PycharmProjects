# coding: utf-8

from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def get_average(path_file):
    df = pd.read_table(path_file, skiprows=10)
    avg = df["LAeq (dBA)"].mean()
    print("Average SPL:", avg)

    return 0


def main():
    path_file = filedialog.askopenfile()
    df = get_average(path_file)
    pass

if __name__ == '__main__':
    main()
