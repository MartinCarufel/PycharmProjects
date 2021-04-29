#coding:utf-8

import os
import tkinter.filedialog
import pandas as pd
from datetime import datetime

def get_file_name_from_path(full_path):
    pl = full_path.split("/")
    return pl[-1]

def get_max_dist(df):
    l = []
    l.append(abs(df.loc[0]["d_min"]))
    l.append(abs(df.loc[0]["d_max"]))
    m = max(l)
    return m


path = tkinter.filedialog.askopenfilenames()
data_bank = [["Cal file name", "1-Sigma", "Max D"]]
for csv_file in path:
    temp_data = []
    df = pd.read_csv(csv_file)
    temp_data.append(get_file_name_from_path(csv_file)[:-4])
    temp_data.append(df.loc[0]["1sig"])
    temp_data.append(get_max_dist(df))
    data_bank.append(temp_data)

final_data = pd.DataFrame(data_bank)
final_data.to_csv("Report.csv")
