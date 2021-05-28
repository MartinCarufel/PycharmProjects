# coding: utf-8

from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

def creat_fig_file_name(path):
    path_list = path.split('/')
    file_name = path_list[-1][:-4]
    return file_name
    print(file_name)
    # print(path_list)


def main():
    print("Hello world")
    avg_dba = {}
    freq_list = []
    value_avg = []
    path_file = filedialog.askopenfile()
    df = pd.read_table(path_file, skiprows=8)
    for col in df:
        if col.endswith("Hz"):
            # print(col)
            freq_list.append(col)
            value_avg.append(df[col].mean())
            # avg_dba[col] = df[col].mean()
        # print(df[col])
    avg_df = pd.DataFrame({'Frequency': freq_list[:], 'dBA': value_avg[:]})
    # avg_df = pd.DataFrame({'Frequency': ['10 Hz', '20 Hz', '30 Hz'], 'dBA': [5, 10, 15]})
    # print(avg_df)

    # plt.show()/

    graph = avg_df.plot.bar(x='Frequency', y='dBA', figsize=(11, 6),  )
    # plt.plot(avg_df)

    creat_fig_file_name(path_file.name)
    plt.savefig(str(creat_fig_file_name(path_file.name)) + ".pdf", bbox_inches='tight')
    plt.show()

    # print(avg_dba)



if __name__ == '__main__':
    main()
