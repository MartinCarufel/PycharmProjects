import pandas as pd
import re
from tkinter import filedialog

sourcefile = filedialog.askopenfile('r')
export_csv = "Export.csv"
df = pd.read_csv(sourcefile, skiprows=7)
pd.set_option('max_columns', None)
date_regex = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9]"
time_regex = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"
am_pm_regex = "AM|PM"


df["Date"] = df['Date/Time'].str.findall(date_regex)
df["Time"] = df['Date/Time'].str.findall(time_regex)
df["AM_PM"] = df['Date/Time'].str.findall(am_pm_regex)

# df['Date'] = df['Date/Time'].str.extract(date_regex, expand=False)
# df["date"] = re.search(date_regex, str(df["Date/Time"])).group(0)
# df["time"] = re.search(time_regex, str(df["Date/Time"])).group(0)
# df["AM_PM"] = re.search(am_pm_regex, str(df["Date/Time"])).group(0)

print(df.shape)
time_in_s = []
time_spend = []

for index, row in df.iterrows():
    cal_time = float(row.Time[0][0:2])*3600 + float(row.Time[0][3:5])*60 + float(row.Time[0][6:8]) + float(row.Time[0][9:12])/1000
    if row.AM_PM[0] == "PM":
        cal_time = cal_time + 12*3600
    # print(row.Time[0][0:2])
    time_in_s.append(cal_time)

first_row = True
for i in range(len(time_in_s)):
    if first_row:
        time_spend.append(0)
        first_row = False
    else:
        time_spend.append(time_spend[i-1] + time_in_s[i] - time_in_s[i-1])

df["Time in s"] = pd.Series(time_in_s)
df["Time spend"] = pd.Series(time_spend)

# df.to_csv(filedialog.asksaveasfilename(defaultextension=".csv"), filetypes=[("Comma Separate", "*.csv")])
mask = [
    ("Comma Separate","*.csv")
]
fout = filedialog.asksaveasfile(
    title="Save As'",
    defaultextension=".csv",
    filetypes=mask)
df.to_csv(fout)
print(df[["Time spend", "CHANNEL0"]])