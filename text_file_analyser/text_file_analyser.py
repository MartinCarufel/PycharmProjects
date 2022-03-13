# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import re

class Text_File_analyser:

    def __init__(self, file):
        self.file = file


    def string_counter(self, string_to_find):
        string_found = 0
        print(self.file)
        with open(self.file, mode='r') as f:
            for line in f:
                if re.search(string_to_find, line) is not None:
                    string_found += 1
        return string_found


    def data_spliter(self, start_with_re, separator_re):
        csv_data = []

        with open(self.file, mode='r') as f:
            for line in f:
                if re.match(start_with_re, line) is not None:
                    new_line = re.sub(pattern=separator_re, repl=",", string=line)[1:-2]
                    csv_data.append(new_line.split(sep=','))
        return csv_data

    def string_extract(self, start_with_re):
        csv_data = []
        with open(self.file, mode='r') as f:
            for line in f:
                if re.match(start_with_re, line) is not None:
                   csv_data.append(line.strip())
                    # new_line = re.sub(pattern=separator_re, repl=",", string=line)[1:-2]
                    # csv_data.append(new_line.split(sep=','))
        return csv_data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

