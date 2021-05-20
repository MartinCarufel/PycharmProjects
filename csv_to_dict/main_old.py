import csv
import pickle

class setting_param():

    def __init__(self, cfg_file):
        self.output_file_name = None
        self.current_cycle = 0
        self.total_cycle = 0



    def load_setting(self):
        pass

    def save_setting(self):
        pass



def csv_to_dict(input_file):
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        mydict = {rows[0]:rows[1] for rows in reader}
    return mydict

def cfg_to_dict(input_file):
    with open(input_file, "r") as f:
        mylist = f.readlines()
        mydict = {}
        for element in range(0, len(mylist)):
            mylist[element] = mylist[element].strip()
        for element in mylist:
            key, value = element.split("=")
            key = key.strip()
            value = value.strip()
            # print(key + "=" + value)
            mydict[key] = value
        # print(mylist)
        # print(mydict)
        # mydict = {rows[0]:rows[1] for rows in reader}
    return mydict

def test_run(nb_iteration):
    for i in range(int(nb_iteration)):
        print(f"Test run {i}")

def save_iteration_done(file_name, current_iteration):
    with open(file_name, "w") as f:
        reader = csv.reader(f)
        mydict = {rows[0]: rows[1] for rows in reader}


def main():
    # program_setting = csv_to_dict("prog_data.csv")
    # for key, value in program_setting.items():
    #     print(key + " : " + value)
    # test_run(program_setting["total cycle"])

    program_setting = cfg_to_dict("prog_data2.csv")
    for key, value in program_setting.items():
        print(key + " : " + value)
    test_run(program_setting["total cycle"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
