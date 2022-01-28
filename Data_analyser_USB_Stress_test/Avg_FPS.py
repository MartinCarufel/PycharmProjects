#coding:utf-8

import os
import tkinter.filedialog
import pandas as pd
from datetime import datetime


path = tkinter.filedialog.askopenfilenames()
time_obj = datetime.now()
time_str = time_obj.strftime("%Y-%m-%d_%H%M%S")


avg_list = []
list_drop_frame = []
for csv_file in path:
    df = pd.read_csv(csv_file)
    # drop_frame = df.loc[(df["#dropped"] > 0)]
    list_drop_frame.append(df["#dropped"].sum())
    avg_list.append(df["avg. fps"].mean())
    # for index, row in drop_frame.iterrows():
    #     list_drop_frame.append([csv_file, row['duration'], row['#dropped'] ])
# df_drop_frame = pd.DataFrame(list_drop_frame, columns =['File', 'Time', 'Drop Frame'])
# print(list_drop_frame)
# print(avg_list)

summary_df = pd.DataFrame()
summary_df["File"] = path
summary_df["drop Frame"] = list_drop_frame
summary_df["Avg FPS"] = avg_list
filename = path[0].split(sep="/")
hp_sn = filename[-1][-12:-4]
summary_df.to_csv("summary_" + hp_sn + ".csv")
# df_drop_frame.to_csv(time_str + '_export_data.csv')
