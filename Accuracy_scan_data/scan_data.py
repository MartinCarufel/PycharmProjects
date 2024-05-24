import pandas as pd


class Data_analyser:

    def __init__(self):
        pass


    def read_csv(self, file_path):
        self.file_path = file_path
        header = ['Scan', 'Mean', 'AMD', 'StdDev', '1sig', '2sig', 'RMS']
        df = pd.read_csv(file_path, skiprows=5, nrows=10, names= header)
        return df









