import pandas as pd
import re
import sys
import os

def Average(lst):
    return sum(lst) / len(lst)

param_file_name = str(sys.argv[1])
hp_serial = param_file_name[15:-4]
# print("---------------")
# print(hp_serial)
# print("---------------")
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

match_data = "\| +[0-9]+.[0-9][0-9]"
match_pattern = "\| +"
header = ["Duration", "# Total Frame", "# total bad pkt",  "# total dropped", "# frames",
            "# dropped", "avg. fps", "MB/s", "#C0 Dead img", "#C1 Dead img", "#C2 Dead img", "#C3 Dead img"]
csv_data = []
with open(param_file_name, mode='r') as f:
    for line in f:
        if re.match(match_data, line) != None:
            new_line = re.sub(pattern=match_pattern, repl=",", string=line)[1:-2]
            # print(new_line)
            csv_data.append(new_line.split(sep=','))
            # csv_data.append(re.split(pattern=match_pattern, string=line))
            # csv_data.append(new_line)

# for i in csv_data:
#     print(i)
# print(csv_data)

df = pd.DataFrame(csv_data, columns=header)
df["Duration"] = df["Duration"].astype(float)
df["avg. fps"] = df["avg. fps"].astype(float)
df["# total dropped"] = df["# total dropped"].astype(int)
# print(df["avg. fps"].mean())
# print(df)
# df.info()
total_drop = []
avg_fps_list = []
avg_fps = []
nb_line, nb_col = df.shape
for i in range(0, nb_line):
    if i == 0:
        avg_fps.append(df["avg. fps"].iloc[i])
    elif float(df["Duration"].iloc[i]) > float(df["Duration"].iloc[i-1]):
        avg_fps.append(df["avg. fps"].iloc[i])
    else:
        total_drop.append(df["# total dropped"].iloc[i])
        avg_fps_list.append(Average(avg_fps))
        avg_fps = []
        avg_fps.append(df["avg. fps"].iloc[i])


# df.to_excel("Export_data " + hp_serial +".xlsx")
df_sumarry = pd.DataFrame()
df_sumarry["Total Drop Frame"] = total_drop
df_sumarry["Total Drop Frame"] = df_sumarry["Total Drop Frame"].astype(int)
df_sumarry["Avg FPS"] = avg_fps_list
df_sumarry["Avg FPS"] = df_sumarry["Avg FPS"].round(decimals=3)
# df_sumarry.to_excel("Export_summary " + hp_serial +".xlsx")
# print(total_drop)
# print(avg_fps_list)
# print(df_sumarry)
# print(df_sumarry.dtypes)

if not os.path.exists("Data_summary.csv"):
    data_summary = open("Data_summary.csv", mode='w')
    data_summary.close()

if os.path.getsize("Data_summary.csv") == 0:
    data_summary = open("Data_summary.csv", mode = 'w')
    data_summary.writelines("Min 1 Drop Frame,Min 1 Avg FPS,Min 2 Drop Frame,Min 2 Avg FPS,Min 3 Drop Frame,Min 3 Avg FPS,Min 4 Drop Frame,Min 4 Avg FPS,Min 5 Drop Frame,Min 5 Avg FPS,Min 6 Drop Frame,Min 6 Avg FPS,Min 7 Drop Frame,Min 7 Avg FPS,Min 8 Drop Frame,Min 8 Avg FPS,Min 9 Drop Frame,Min 9 Avg FPS,Min 10 Drop Frame,Min 10 Avg FPS\n")
    for index, row in df_sumarry.iterrows():
        data_summary.write(str(row["Total Drop Frame"]) + ',' + str(row["Avg FPS"]) + ',')
    data_summary.write("\n")
    data_summary.close()

else:
    data_summary = open("Data_summary.csv", mode='a')
    for index, row in df_sumarry.iterrows():
        # print(int(row["Total Drop Frame"]))
        data_summary.write(str(int(row["Total Drop Frame"])) + ',' + str(row["Avg FPS"]) + ',')
    data_summary.write("\n")
    data_summary.close()
