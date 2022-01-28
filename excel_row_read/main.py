#coding:utf-8

import openpyxl
import xlrd



wb = openpyxl.load_workbook("Exemple1.xlsx")
ws = wb["Patate"]
line_not_empty = True
test_row = 1
while line_not_empty:
    line_not_empty = False
    for row in ws.iter_rows(min_row=test_row, max_col=None, max_row=test_row, values_only=True):
        print(row)
        for value in row:
            # print(line_not_empty)
            if value != None:
                line_not_empty = line_not_empty | True
            elif value == None:
                line_not_empty = line_not_empty | False
        if line_not_empty == False:
            print("Ligne vide {}".format(test_row))
            break

    test_row += 1

