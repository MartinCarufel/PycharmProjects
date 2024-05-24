import pandas as pd


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










