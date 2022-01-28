"""
Program to re format the data from Treacable Trac to excel

Usage: python "Log converter.py" <file name to convert>

"""
import pandas as pd
import sys

input_file = sys.argv[1]
daily_h_log = sys.argv[2]

def convert_date(pd_serie):
	new_date_format = []
	for i in pd_serie:
		new_date_format.append(i[-4:] + "-" + i[0:2] + "-" + i[3:5])
	return new_date_format

def convert_rh(pd_serie):
	new_rh_format = []
	for i in pd_serie:
		new_rh_format.append(i[1:3])
	return new_rh_format


#input file
fin = open(input_file, "rt")
#output file to write the result to
file_out_name = input_file[:-4] + "_mod.CSV"
fout = open(file_out_name, "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('\0', ''))
#close input and output files
fin.close()
fout.close()

df_org = pd.read_csv(file_out_name, skiprows=5)
date_converted = []
time = []
rh = []
temperature = []
atm = []

rh = df_org["CH1 (%)"]

df_new = pd.DataFrame()
# df_new["Date"] = df_org["Date"]
df_new["Date"] = convert_date(df_org["Date"])
df_new["Time"] = df_org["Time"]
# df_new["RH (%)"] = df_org["CH1 (%)"]
df_new["RH (%)"] = convert_rh(df_org["CH1 (%)"])
df_new["Temp (°C)"] = df_org["CH2 (C)"]
df_new["Press Atm (mb)"] = df_org["CH3 (mb)"]
# print(rh)
print(df_new)
df_result = df_new.loc[df_new["Time"].str.contains(daily_h_log)]
print(df_result)


writer = pd.ExcelWriter("log.xlsx", engine = 'xlsxwriter')
df_new.to_excel(writer, sheet_name = 'Full log')
df_result.to_excel(writer, sheet_name = 'Daily log')
writer.save()
writer.close()