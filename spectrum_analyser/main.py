# coding: utf-8

from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def create_fig_file_name(path):
    path_list = path.split('/')
    file_name = path_list[-1][:-4]
    return file_name
    print(file_name)


def create_plot(avg_df, path_file):
    avg_df.plot.bar(y='dBA', figsize=(11, 6), )
    create_fig_file_name(path_file.name)
    plt.savefig(path_file.name[:-4] + ".pdf", bbox_inches='tight')
    plt.show()


def create_avg_data(path_file):
    df = pd.read_table(path_file, skiprows=8)
    df = df.drop(columns=["Time (s):  / Midband frequencies"])
    avg_df = df.mean(axis=0, )
    avg_df = pd.DataFrame(avg_df, columns=["dBA"])
    avg_df.to_csv("data.csv")
    return avg_df


def main():
    path_file = filedialog.askopenfile()
    avg_df = create_avg_data(path_file)
    create_plot(avg_df, path_file)


if __name__ == '__main__':
    main()
