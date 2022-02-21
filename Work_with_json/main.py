import json
import pandas as pd
from tkinter import filedialog
import re


class Json_data_analyser:

    def __init__(self, file):
        self.input_file = file
        self.unique_id = []
        self.processed_data = []

    def extract_file_list(self):
        path_file = self.input_file
        files = []
        with open(path_file) as pf:
            files = pf.read().splitlines()
        # print(files)
        return files

    def create_unique_id(self, path_list):

        for file in path_list:
            ser = re.search("sn\d{6,6}", file)
            self.unique_id.append(file[ser.start() + 2:ser.end()])

    def build_dataframe(self, path_list):
        self.path_list = path_list
        for idx in range(len(self.path_list)):
            row_to_add = []
            row_to_add.append(self.unique_id[idx])

            with open(path_list[idx], 'r') as f:
                json_file = json.load(f)
            row_to_add.append(json_file[0]["data"]["vbusRef"])
            row_to_add.append(json_file[0]["data"]["dcr"]["gnd"])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbus"])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['up'][0])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['up'][1])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['up'][2])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['up'][3])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['down'][0])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['down'][1])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['down'][2])
            row_to_add.append(json_file[0]["data"]["dcr"]["gndPin"]['down'][3])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['up'][0])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['up'][1])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['up'][2])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['up'][3])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['down'][0])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['down'][1])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['down'][2])
            row_to_add.append(json_file[0]["data"]["dcr"]["vbusPin"]['down'][3])
            row_to_add.append(json_file[0]['data']['signalIntegrity'][0]['heo'])
            row_to_add.append(json_file[0]['data']['signalIntegrity'][0]['veo'])
            row_to_add.append(json_file[0]['data']['signalIntegrity'][1]['heo'])
            row_to_add.append(json_file[0]['data']['signalIntegrity'][1]['veo'])
            self.processed_data.append(row_to_add)
        self.data = pd.DataFrame(self.processed_data)
        # print(self.data)

    def avg_value(self):
        l = list(dict.fromkeys(self.unique_id))
        sdb = pd.DataFrame()

        # print(len(sdb.index))
        for id in l:
            # print(id)
            (x, y) = self.data.shape
            x = self.data.loc[self.data[0] == id, 1:y-1].mean()
            # df.loc[df[0] == i, 1:3].mean()
            sdb[id] = x
            # print(x)
        sdb.index = ['vbusRef', 'gnd', 'vbus', 'gnd pin U-A1', 'gnd pin U-A12', 'gnd pin U-B1', 'gnd pin U-B12',
                     'gnd pin D-A1', 'gnd pin D-A11', 'gnd pin D-B2', 'gnd pin D-B12', 'vBus pin U-A1', 'vBus pin U-A12',
                     'vBus pin U-B1', 'vBus pin U-B12','vBus pin D-A1', 'vBus pin D-A11', 'vBus pin D-B2', 'vBus pin D-B12',
                     'Rx HEO', 'Rx VEO', 'Tx HEO', 'Tx VEO']
        print(sdb)

def main(name):
    json_data = Json_data_analyser(filedialog.askopenfilename())
    files = json_data.extract_file_list()
    json_data.create_unique_id(files)
    json_data.build_dataframe(files)
    json_data.avg_value()


if __name__ == '__main__':
    main('PyCharm')
