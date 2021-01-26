import re


true_list = ["a1", "ab1", "a12", "a1235", "AS123", "Sa1"]
false_list = ["1a", "aa", "11", "a1a"]

for cell_name in true_list:

    result = re.search("^[A-Z]+[0-9]+$", cell_name.upper())
    if result != None:
        print("OK")
    else:
        print("test %s failed" %cell_name)

for cell_name in false_list:

    result = re.search("^[A-Z]+[0-9]+$", cell_name.upper())
    if result == None:
        print("OK")
    else:
        print("test %s failed" %cell_name)