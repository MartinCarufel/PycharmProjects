# coding: utf-8

from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from os import system

def get_continue():
    while True:
        response = input("Do you want to import new file (Y/N): ").upper()

        if response == 'Y':
            return True
        elif response == 'N':
            return False
        else:
            print("Please make sure to answer only by Y/N")


def get_all_file_to_analysis():
    new_file = True
    file_list = []
    while new_file:
        file_list.append(filedialog.askopenfile().name)
        system('cls')
        print_file_loaded(file_list)
        new_file = get_continue()
    return file_list

def print_file_loaded(file_list):

    for path in file_list:
        file_name = path.split("/")[-1]
        print(file_name)


def mean_value(path_file, freq_band):
    df = pd.read_table(path_file, skiprows=8)
    avg = df[freq_band].mean()
    return avg


def data_analyser(file_list):
    freq_band_to_analyze = ["25 Hz", "31.5 Hz", "40 Hz", "50 Hz", "63 Hz", "80 Hz", "100 Hz", "125 Hz", "160 Hz", "200 Hz",
                            "250 Hz", "315 Hz", "400 Hz", "500 Hz", "630 Hz", "800 Hz", "1000 Hz", "1250 Hz", "1600 Hz",
                            "2000 Hz", "2500 Hz", "3150 Hz", "4000 Hz", "5000 Hz", "6300 Hz", "8000 Hz", "10000 Hz",
                            "12500 Hz", "16000 Hz", "Global"]
    mean_value_per_freq = {}
    for freq in freq_band_to_analyze:
        mean_value_list = []
        for file in file_list:
            mean_value_list.append(mean_value(file, freq))
        mean_value_per_freq[freq] = mean_value_list
    return mean_value_per_freq


def plot_bar_graph(data, timestamp):
    fig, axes = plt.subplots(ncols=6, nrows=5, figsize=(25, 15))
    freq_band_to_plot = [["25 Hz", "31.5 Hz", "40 Hz", "50 Hz", "63 Hz", "80 Hz"],
                         ["100 Hz", "125 Hz", "160 Hz", "200 Hz", "250 Hz", "315 Hz"],
                         ["400 Hz", "500 Hz", "630 Hz", "800 Hz", "1000 Hz", "1250 Hz"],
                         ["1600 Hz", "2000 Hz", "2500 Hz", "3150 Hz", "4000 Hz", "5000 Hz"],
                         ["6300 Hz", "8000 Hz", "10000 Hz", "12500 Hz", "16000 Hz", "Global"]]
    for col in range(6):
        for row in range(5):
            try:
                data[freq_band_to_plot[row][col]].plot.bar(ax=axes[row][col])
                axes[row][col].set_title(freq_band_to_plot[row][col], fontsize=10)
            except IndexError:
                pass
    fig.subplots_adjust(top=0.975, bottom=0.05, left=0.025, right=0.99, hspace=0.5, wspace=0.2)
    plt.savefig("data_" + timestamp + ".png")


def main():
    ct = datetime.now().isoformat(timespec='seconds').replace(':', '')
    file_list = get_all_file_to_analysis()
    # file_list = ["Spectrum_data_2021-07-05_10_58_39 golden unit.tsv",
    #              "Spectrum_data_2021-07-05_11_04_08 disp 400 pre-conditioning.tsv",
    #              "Spectrum_data_2021-07-05_11_07_01 401 pre-conditioning.tsv", "Spectrum_data_2021-07-05_10_58_39 golden unit.tsv",
    #              "Spectrum_data_2021-07-05_11_04_08 disp 400 pre-conditioning.tsv",
    #              "Spectrum_data_2021-07-05_11_07_01 401 pre-conditioning.tsv","Spectrum_data_2021-07-05_10_58_39 golden unit.tsv",
    #              "Spectrum_data_2021-07-05_11_04_08 disp 400 pre-conditioning.tsv",
    #              "Spectrum_data_2021-07-05_11_07_01 401 pre-conditioning.tsv",
    #              "Spectrum_data_2021-07-05_11_07_01 401 pre-conditioning.tsv"]
    data = pd.DataFrame(data=data_analyser(file_list))
    try:
        data.to_csv("data_" + ct + ".csv")
    except PermissionError:
        save_file_name = filedialog.asksaveasfile().name
        data.to_csv(save_file_name)

    plot_bar_graph(data, ct)
    # plt.show()
    print("Done")


if __name__ == '__main__':
    main()

import os
os.getgroups()