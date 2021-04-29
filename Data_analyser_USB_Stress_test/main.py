#coding:utf-8

import os
import tkinter.filedialog
import pandas as pd
from datetime import datetime


path = tkinter.filedialog.askopenfilenames()
time_obj = datetime.now()
time_str = time_obj.strftime("%Y-%m-%d_%H%M%S")
list_drop_frame = []
for csv_file in path:
    df = pd.read_csv(csv_file)
    drop_frame = df.loc[(df["#dropped"] > 0)]
    for index, row in drop_frame.iterrows():
        list_drop_frame.append([csv_file, row['duration'], row['#dropped'] ])
df_drop_frame = pd.DataFrame(list_drop_frame, columns =['File', 'Time', 'Drop Frame'])

df_drop_frame.to_csv(time_str + '_export_data.csv')
