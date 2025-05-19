from docx import Document
import os
import pandas as pd
import openpyxl
import re

class Extrace_req:
    """
        Class to handle the extraction of requirement references from DOCX files.
        """
    def __init__(self):
        pass

    def list_folder(self, path):
        """
                Lists all file paths in the specified directory.

                Args:
                    path (str): The folder path.

                Returns:
                    list: List of full file paths.
                """
        folder_path = path  # Change this to your folder path
        file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return file_paths

    def extract_req_from_doc(self, files_list):
        """
               Extracts requirements from the first table of each DOCX file.

               Args:
                   files_list (list): List of DOCX file paths.

               Returns:
                   dict: Dictionary mapping document numbers to extracted requirements.
               """
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
        """
                Extracts the document number from the file path.

                Args:
                    path (str): Full file path.

                Returns:
                    str: First 10 characters of the file name.
                """
        sep_path = path.split("\\")
        return sep_path[-1][0:10]
        pass

    def _create_array_of_req(self, text):
        """
               Extracts requirement IDs in the format `X.XXX` using regex.

               Args:
                   text (str): Text content from the DOCX cell.

               Returns:
                   list: List of matching requirement references.
               """
        cleaned_list = re.findall(r"[0-9]{1,3}\.[0-9]{3}", text)

        #
        # first_line = text.split("\n")[0]
        # first_line = first_line.replace(";", ",")
        # req_split = first_line.split(", ")
        # cleaned_list = [re.sub(r"\[[0-9]\]", "", s) for s in req_split]
        # cleaned_list = [s.rstrip() for s in cleaned_list]
        return cleaned_list

    def pd_dataframe_from_dict(self, data):
        """
                Converts a dictionary to a Pandas DataFrame.

                Args:
                    data (dict): Dictionary to convert.

                Returns:
                    pd.DataFrame: Converted DataFrame.
                """
        df = pd.DataFrame.from_dict(data, orient="index").T
        return df

class Excel_manager:
    """
        Class to manage Excel operations using openpyxl.
        """
    def __init__(self):
        pass

    def open_excel(self, file, sheet):
        """
                Opens an Excel file and selects a worksheet.

                Args:
                    file (str): Excel file path.
                    sheet (str): Sheet name to open.

                Returns:
                    Worksheet object.
                """
        self.wb = openpyxl.load_workbook(file)
        self.ws = self.wb[sheet]
        return self.ws

    def read_col_extract_PRS(self):
        """
                Reads column B and extracts all values starting with 'PR_'.

                Returns:
                    list: List of requirement IDs (e.g., PR_1234).
                """
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
        """
                Finds the cell in a column matching a specific value.

                Args:
                    value (str): Cell value to find.
                    col (str): Column letter (e.g., 'B').

                Returns:
                    Cell object if found, else None.
                """
        col = self.ws[col]
        for c in col:
            if c.value == value:
                return c

    def truncate(self, data):
        """
               Truncates the first 3 characters from a string.

               Args:
                   data (str): Input string.

               Returns:
                   str: Truncated string.
               """
        return data[3:]

    def marking(self, col_to_mark, req_list):
        """
                Marks an 'x' in the specified column for each requirement ID.

                Args:
                    col_to_mark (str): Excel column to mark.
                    req_list (list): List of requirement IDs (without 'PR_' prefix).
                """
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
    """
        Main execution function that:
        - Maps document IDs to Excel columns.
        - Extracts requirements from DOCX files.
        - Marks corresponding cells in the Excel sheet.
        - Saves the result in a new Excel file.
        """
    col_id_relation = {
"DEV-0044559": "G",
"DEV-0044560": "H",
"DES73-6607": "I",
"DEV-0044561": "J",
"DEV-0044562": "K",
"DEV-0044568": "L",
"DEV-0044563": "M",
"DEV-0044564": "N",
"DEV-0044565": "O",
"DEV-0044569": "P",
"DEV-0044566": "Q",
"DEV-0044567": "R",
"DEV-0044567": "S",
"DEV-0044573": "T",
"DEV-0044574": "U",
"DEV-0044575": "V",
"DEV-0044576": "W",
"DEV-0044577": "X",
"DEV-0044579": "Y",
"DEV-0044581": "Z",
"DEV-0044580": "AA",
"DEV-0044571": "AB",
"DEV-0044600": "AC",
"DEV-0044597": "AD",
"DEV-0044601": "AE",
"DEV-0044602": "AF",
"DEV-0044629": "AG",
"DEV-0044623": "AH",
"DEV-0044621": "AI",
"DEV-0045649": "AJ",
"DEV-0045608": "AK",
"DEV-0045609": "AL",
"DEV-0044596": "AM",
"DEV-0044594": "AN",
"DEV-0044593": "AO",
"DEV-0044625": "AP",
"DEV-0044628": "AQ",
"DEV-0044604": "AR",
"DEV-0044605": "AS",
"DEV-0044612": "AT",
"DEV-0044606": "AU",
"DEV-0044607": "AV",
"DEV-0044608": "AW",
"DEV-0044609": "AX",
"DEV-0044610": "AY",
"DEV-0044578": "AZ",
"DEV-0044611": "BA",
"DEV-0044599": "BB",
"DEV-0044599": "BC",
"DEV-0044656": "BD",
"DEV-0044650": "BE",
"DEV-0044591": "BF",
"DEV-0044646": "BG",
"DEV-0044613": "BH",
"DEV-0044592": "BI",
"DEV-0044643": "BJ",
"UC_007": "BK",
"UC_008": "BL",
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
