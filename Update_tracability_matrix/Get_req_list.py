from docx import Document
import os
import pandas as pd
import openpyxl
import re

class Extrace_req:
    def __init__(self):
        pass

    def list_folder(self, path):
        folder_path = path  # Change this to your folder path
        file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return file_paths

    def extract_req_from_doc(self, files_list):
        result = {}
        for file in files_list:
            doc = Document(file)
            tbl = doc.tables[0]
            cell = tbl.cell(2, 1)
            text = cell.text
            result[(self._extract_doc_number_from_path(file))] = self._create_array_of_req(text)
            # print("{};{}".format(file, text))
        return result

    def _extract_doc_number_from_path(self, path):
        sep_path = path.split("\\")
        return sep_path[-1][0:10]
        pass

    def _create_array_of_req(self, text):
        cleaned_list = re.findall(r"[0-9]{1,3}\.[0-9]{3}", text)

        #
        # first_line = text.split("\n")[0]
        # first_line = first_line.replace(";", ",")
        # req_split = first_line.split(", ")
        # cleaned_list = [re.sub(r"\[[0-9]\]", "", s) for s in req_split]
        # cleaned_list = [s.rstrip() for s in cleaned_list]
        return cleaned_list

    def pd_dataframe_from_dict(self, data):
        df = pd.DataFrame.from_dict(data, orient="index").T
        return df

class Excel_manager:

    def __init__(self):
        pass

    def open_excel(self, file, sheet):
        self.wb = openpyxl.load_workbook(file)
        self.ws = self.wb[sheet]
        return self.ws

    def read_col_extract_PRS(self):
        prs_list = []
        col = self.ws['B']
        for c in col:
            try:
                if c.value[0:3] == "PR_":
                    prs_list.append(c.value)
            except TypeError:
                pass
        return prs_list

    def cell_coord(self, value, col):
        col = self.ws[col]
        for c in col:
            if c.value == value:
                return c

    def truncate(self, data):
        return data[3:]

    def marking(self, col_to_mark, req_list):
        for req in req_list:
            req = "PR_{}".format(req)
            cell_row = self.cell_coord(req, "B")
            try:
                cell = "{}{}".format(col_to_mark, cell_row.row)
                self.ws[cell].value = "x"
            except Exception as e:
                print(f"The text requirement is: {req}")
                print(f"{e}")
def main():
    col_id_relation = {"DES73-6894": "G",
                       "DES73-6606": "H",
                       "DES73-6607": "I",
                       "DES73-6896": "J",
                       "DES73-6897": "K",
					   "DES73-6985": "L",
                       "DES73-6881": "M",
                       "DES73-6973": "N",
                       "DES73-6877": "O",
                       "DES73-6997": "P",
                       "DES73-6878": "Q",
                       "DES73-6984": "R",
                       "DES73-6895": "S",
                       "DES73-6900": "T",
                       "DES73-6901": "U",
                       "DES73-6902": "V",
                       "DES73-6904": "W",
                       "DES73-6882": "X",
                       "DES73-6905": "Y",
                       "DES73-7095": "Z",
                       "DES73-6899": "AA",
                       "DES73-7100": "AB",
                       "DES73-6911": "AC",
                       "DES73-6891": "AD",
                       "DES73-6912": "AE",
                       "DES73-6917": "AF",
                       "DES73-6947": "AG",
                       "DES73-7004": "AH",
                       "DES73-6982": "AI",
                       "DES73-6599": "AJ",
                       "DES73-6563": "AK",
                       "DES73-6597": "AL",
                       "DES73-7006": "AM",
                       "DES73-7008": "AN",
                       "DES73-6923": "AO",
                       "DES73-6924": "AP",
                       "DES73-6938": "AQ",
                       "DES73-6925": "AR",
                       "DES73-6926": "AS",
                       "DES73-6927": "AT",
                       "DES73-6928": "AU",
                       "DES73-6929": "AV",
                       "DES73-6890": "AW",
                       "DES73-6930": "AX",
                       "DES73-6893": "AY",
                       "DES73-7107": "AZ",
                       "DES73-7099": "BA",
                       "DES73-7087": "BB",
                       "DES73-6908": "BC",
                       "DES73-6966": "BD",
                       "DES73-6943": "BE",
                       "DES73-6909": "BF",
                       "DES73-6945": "BG"
                       }

    o = Extrace_req()
    exl = Excel_manager()
    ws = exl.open_excel("DEL73-6871 STMN IOS Software Traceability Matrix (v1.2)_Effective.xlsx", "1.0.2")
    folder_list = [r"C:\Users\u120230\temp\SDD", r"C:\Users\u120230\temp\VER", r"C:\Users\u120230\temp\VAL"]

    for folder in folder_list:
        file_list = o.list_folder(folder)
        result = o.extract_req_from_doc(file_list)
        for key, value in result.items():
            print(key)
            exl.marking(col_id_relation[key], value)
    exl.wb.save("out.xlsx")


if __name__ == "__main__":
    main()
