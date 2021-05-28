# coding: utf-8

from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

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
    print(avg_df)
    graph = avg_df.plot.bar(x='Frequency', y='dBA')
    # plt.plot(avg_df)

    plt.show()

    # print(avg_dba)



if __name__ == '__main__':
    main()
