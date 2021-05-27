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
    avg_df = pd.DataFrame({'Frequency':freq_list[:], 'dbA':value_avg[:]})
    print(avg_df)
    graph = df.plot.bar(x='Frequency', y='dbA', rot=0)
    # plt.plot(avg_df)

    plt.show()

    # print(avg_dba)



if __name__ == '__main__':
    main()
