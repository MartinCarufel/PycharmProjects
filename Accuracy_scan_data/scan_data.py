import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

class Data_analyser:

    def __init__(self):
        pass


    def read_csv(self, file_path):
        self.file_path = file_path
        header = ['Scan', 'Mean', 'AMD', 'StdDev', '1sig', '2sig', 'RMS']
        df = pd.read_csv(file_path, skiprows=5, nrows=10, names= header)
        return df

    def value_within_range_count(self, range_min, range_max, df_col):
        """

        :param range_min:
        :param range_max:
        :param data: dataframe colum to be analysed ex: df['max']
        :return:
        """
        count = 0
        # print(f'range_min: {range_min}')
        # print(f'range_max: {range_max}')
        for data in df_col:
            # print(f'Data analisé: {data}')
            if range_min < data <= range_max:
                count = count + 1
        return count

    def create_range_index(self, range):
        range_index = []

        for i in range[1:]:
            range_index.append("{} - {}".format(int((i-0.004)*1000), int(i*1000)))
        return range_index


    def plot_bar_graph(self, data_df):
        plt.figure(figsize=(10, 6))
        plt.bar(data_df['range'], data_df['Martin scan'], color='blue')
        plt.ylabel('Value')
        plt.xlabel('RMS Deviation', rotation=0, labelpad=20)
        plt.xticks(rotation=90)
        plt.gca().yaxis.set_major_formatter(PercentFormatter())
        plt.show()


    def convert_list_in_purcentage(self, list_in):
        converted_list = []
        sum_of_element = sum([x for x in list_in])

        for i in list_in:
            converted_list.append(i/sum_of_element*100)

        return converted_list

def main():

    data_class = Data_analyser()
    range_band = [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060, 0.065,
                               0.070, 0.075, 0.080]
    df = data_class.read_csv("./Test_data/batchMetrologySummary.csv")
    data_table = []
    for i in range(len(range_band) - 1):
        data_table.append(data_class.value_within_range_count(range_band[i], range_band[i + 1], df['RMS']))
    data_table = data_class.convert_list_in_purcentage(data_table)
    print(data_table)


    result_df = pd.DataFrame()
    index = data_class.create_range_index(range_band)
    result_df['range'] = index
    result_df['Martin scan'] = data_table

    print(result_df)
    data_class.plot_bar_graph(result_df)

if __name__ == '__main__':
    main()


