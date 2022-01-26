import pandas as pd

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
fin = open("B9C3826B.CSV", "rt")
#output file to write the result to
fout = open("B9C3826B_mod.CSV", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('\0', ''))
#close input and output files
fin.close()
fout.close()

df_org = pd.read_csv("B9C3826B_mod.CSV", skiprows=5)
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

df_new.to_excel("log.xlsx")