# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import pandas as pd
from tkinter import filedialog
import re


class Json_data_analyser:

    def __init__(self, file):
        self.input_file = file
        # self.files = file
        self.unique_id = []
        # self.processed_data = pd.DataFrame()
        self.processed_data = []
        # self.data = pd.DataFrame()
        # self.col = ['A', 'B', 'C', 'D']
        pass

    def extract_file_list(self):
        path_file = self.input_file
        # path_file = filedialog.askopenfilename()
        files = []
        with open(path_file) as pf:
            files = pf.read().splitlines()
        print(files)
        return files

    def create_unique_id(self, path_list):

        for file in path_list:
            ser = re.search("sn\d{6,6}", file)
            self.unique_id.append(file[ser.start() + 2:ser.end()])

    def build_dataframe(self, path_list):
        # self.json_tags = json_tags
        self.path_list = path_list
        for idx in range(len(self.path_list)):
            row_to_add = []
            row_to_add.append(self.unique_id[idx])

            with open(path_list[idx], 'r') as f:
                json_file = json.load(f)
            row_to_add.append(json_file[0]["data"]["dcr"]["gnd"])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbus"])
            # for json_tag in json_tags:
            #     self.processed_data[col_id] =
            #     pass
            self.processed_data.append(row_to_add)
            pass
        self.data = pd.DataFrame(self.processed_data)
        print(self.data)

    def avg_value(self):
        l = list(dict.fromkeys(self.unique_id))
        sdb = pd.DataFrame()
        for id in l:
            # print(id)
            x = self.data.loc[self.data[0] == id, 1:2].mean()
            # df.loc[df[0] == i, 1:3].mean()
            sdb[id] = x
            print(x)
        sdb.index = ['gnd', 'vbus']
        print(sdb)
    pass

def main(name):
    # Use a breakpoint in the code line below to debug your script.

    """
    path_file = filedialog.askopenfilename()
    files = []
    with open(path_file) as pf:
        files = pf.read().splitlines()
    print(files)"""

    json_data = Json_data_analyser(filedialog.askopenfilename())
    files = json_data.extract_file_list()
    json_data.create_unique_id(files)
    json_data.build_dataframe(files)
    json_data.avg_value()

"""
    cbl_ser = []
    dcr_gnd = []
    dcr_vbus = []
    for file in files:
        with open(file, 'r') as f:
            json_file = json.load(f)
        # print(file.name)
        ser = re.search("sn\d{6,6}", file)

        # ser = re.search("sn", file.name)
        cbl_ser.append(file[ser.start()+2:ser.end()])
        dcr_gnd.append(json_file[0]["data"]["dcr"]["gnd"])
        dcr_vbus.append(json_file[0]["data"]["dcr"]["vbus"])
        # print(json_file[0]["data"]["dcr"]["gnd"])
        # print(json_file[0]["data"]["dcr"]["vbus"])
        # print(json_file[0]["data"]["resultCodes"][0]["code"])
        # < array >\ < element  # 0>\data\resultCodes\<element #0>

        # ser1 = ["a", "b", "c"]
        # ser2 = [2, 3, 4]
        #
    df = pd.DataFrame()
    df["Cable Serial"] = cbl_ser
    df["DC Resistance GND"] = dcr_gnd
    df["DC Resistance Vbus"] = dcr_vbus
    print(df)

    df_sumarry = pd.DataFrame()
    list_serial = df["Cable Serial"].unique()
    dcr_gnd_avg = []
    for serial in list_serial:
        dcr_gnd_avg.append(df.loc[df["Cable Serial"]==serial, "DC Resistance GND"].mean())
        pass
        # dcr_gnd_avg.append(df.loc[df["Cable Serial"]==serial].mean())
    # ndf = df.loc[df["Cable Serial"]=="275081", df["DC Resistance GND"]]
    # ndf = df.loc[df["Cable Serial"]=="275081", "DC Resistance GND"].mean()
    print(list_serial)
    # print(ndf)
    print(dcr_gnd_avg)"""
# Press the green button
# in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
