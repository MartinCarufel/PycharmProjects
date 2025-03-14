import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Data_analyser:
    """
    Input the file created by the Accuracy software tool batchMetrologySummary.csv
    And it generate an accuracy distribution table  in range by setp of 5 micron.
    """

    def __init__(self):
        self.entry_box_text = ""
        self.var_ask_continue = True

        pass


    def read_csv(self, file_path):

        """
        Read the result from Software Accuracy Software Tool and get the first result
        :param file_path: file path
        :return: pandas dataframe
        """

        self.file_path = file_path
        header = ['Scan', 'Mean', 'AMD', 'StdDev', '1sig', '2sig', 'RMS']
        # df = pd.read_csv(file_path, skiprows=5, nrows=10, names= header)
        df = pd.read_csv(file_path, skiprows=5, names=header, skip_blank_lines=False)
        blank_df = df.loc[df.isnull().all(1)]
        if len(blank_df) > 0:
            first_blank_index = blank_df.index[0]
            df = df[:first_blank_index]
        # print(df)
        return df

    def value_within_range_count(self, range_min, range_max, df_col):
        """
        Count the number of result that meet the minimum value and max passed in arg.
        :param range_min:
        :param range_max:
        :param data: dataframe colum to be analysed ex: df['max']
        :return: int count of number occurence
        """
        count = 0
        # print(f'range_min: {range_min}')
        # print(f'range_max: {range_max}')
        for data in df_col:
            # print(f'Data analisé: {data}')
            if range_min < float(data) <= range_max:
                count = count + 1
        return count

    def create_range_index(self, range):
        """
        Create the range tag with interval of 5 ex: 1 to 5, 6 to 10 ....
        :param range: list of values
        :return: list of string label the interval ex: '1 - 5'
        """
        range_index = []

        for i in range[1:]:
            range_index.append("{} - {}".format(int(i*1000)-4, int(i*1000)))
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
        # print(sum_of_element)
        for i in list_in:
            converted_list.append((i/sum_of_element)*100)
        return converted_list

    def select_file(self):
        return filedialog.askopenfilename()

    def choose_data_name(self):
        self.root = tk.Tk()
        self.root.title("Enter the data name")
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(padx=10, pady=10)
        button = tk.Button(self.root, text="OK", command=self._kill_entry_window)
        button.pack(pady=10, ipadx=20)
        self.entry.focus_set()
        self.entry.bind('<Return>', self._kill_entry_window)
        self.entry.focus_set()
        self.root.mainloop()


    def _kill_entry_window(self, *args):
        self.entry_box_text = self.entry.get()
        self.root.destroy()

    def ask_continue(self):
        self.win_cont = tk.Tk()
        self.win_cont.title("More data ?")
        self.win_cont.geometry("300x80")
        label = tk.Label(self.win_cont, text="Do you want to process more data ?")
        label.grid(row=0, column=0, columnspan=2)
        button_yes = tk.Button(self.win_cont, text="YES", command=self._cont_set_true)
        button_no = tk.Button(self.win_cont, text="NO", command=self._cont_set_false)
        button_yes.grid(row=1, column=0, pady=5, ipadx=20, padx=20)
        button_no.grid(row=1, column=1, pady=5, ipadx=20, padx=20)
        self.win_cont.mainloop()

    def _cont_set_true(self):
        self.var_ask_continue = True
        self.win_cont.destroy()  # Optionally close the window

    def _cont_set_false(self):
        self.var_ask_continue = False
        self.win_cont.destroy()  # Optionally close the window

    def split_cvs_blocks(self, file_path):
        """This function find line number for each text block
        return: List of tupple start , end of each text block"""

        self.file_path = file_path
        header = ['Scan', 'Mean', 'AMD', 'StdDev', '1sig', '2sig', 'RMS']

        blocks = []
        start_line = None
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip():  # If the line is not empty
                if start_line is None:
                    start_line = i + 1  # Line numbers start from 1
            else:
                if start_line is not None:
                    end_line = i
                    blocks.append((start_line, end_line))
                    start_line = None

            # Handle the last block if the file does not end with an empty line

        if start_line is not None:
            blocks.append((start_line, len(lines)))

        return blocks

    def read_cvs_block(self, file_path, block):
        self.block = block
        self.file_path = file_path
        header = ['Scan', 'Mean', 'AMD', 'StdDev', '1sig', '2sig', 'RMS']
        df = pd.read_csv(file_path, skiprows=int(block[0])+3, nrows=int(block[1])-(int(block[0]+3)), names=header)
        # df = pd.read_csv(file_path, skiprows=5, names=header, skip_blank_lines=False)
        return df

def main():

    data_class = Data_analyser()
    range_band = [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060, 0.065,
                               0.070, 0.075, 0.080]
    df = data_class.read_csv("./Test_data/batchMetrologySummary.csv")
    data_table = []
    for i in range(len(range_band) - 1):
        data_table.append(data_class.value_within_range_count(range_band[i], range_band[i + 1], df['RMS']))
    data_table = data_class.convert_list_in_purcentage(data_table)
    # print(data_table)


    result_df = pd.DataFrame()
    index = data_class.create_range_index(range_band)
    result_df['range'] = index
    result_df['Martin scan'] = data_table

    # print(result_df)
    data_class.plot_bar_graph(result_df)

def main_2():
    data_class = Data_analyser()
    range_band = [0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060, 0.065,
                  0.070, 0.075, 0.080]

    result_df = pd.DataFrame()
    index = data_class.create_range_index(range_band)
    result_df['range'] = index

    while data_class.var_ask_continue:
        file_path = data_class.select_file()
        result_blocks = data_class.split_cvs_blocks(file_path)
        df = data_class.read_cvs_block(file_path, result_blocks[-3:-2][0])

        # df = data_class.read_csv(data_class.select_file())
        data_class.choose_data_name()
        data_set_name = data_class.entry_box_text
        data_table = []
        for i in range(len(range_band) - 1):
            data_table.append(data_class.value_within_range_count(range_band[i], range_band[i + 1], df['RMS']))
        data_table = data_class.convert_list_in_purcentage(data_table)
        result_df[data_set_name] = data_table
        data_class.ask_continue()
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d_%H%M%S")
    # result_df.to_csv(f"Repro_analysis_{formatted_now}.csv")
    result_df.to_excel(f"Repro_analysis_{formatted_now}.xlsx")
    # print(result_df)

if __name__ == '__main__':
    main_2()


