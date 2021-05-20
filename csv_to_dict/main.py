import csv
import pickle
from os import path


class setting_param():

    def __init__(self, file):
        
        self.parameter = self.cfg_to_dict(file)


    def cfg_to_dict(self, input_file):
        with open(input_file, "r") as f:
            mylist = f.readlines()
            mydict = {}
            for element in range(0, len(mylist)):
                mylist[element] = mylist[element].strip()
            for element in mylist:
                key, value = element.split("=")
                key = key.strip()
                try:
                    value = int(value.strip())
                except:
                    value = value.strip()
                # print(key + "=" + value)
                mydict[key] = value
            # print(mylist)
            # print(mydict)
            # mydict = {rows[0]:rows[1] for rows in reader}
        return mydict

    def update_param(self, param_name, param_value):
        self.parameter[param_name] = param_value
        # print(self.param_name)
        pass

    def read_param(self, param_name):
        pass


def csv_to_dict(input_file):
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        mydict = {rows[0]:rows[1] for rows in reader}
    return mydict


def test_run(prog_setting):
    output_file = prog_setting.parameter["output file name"]
    current_iteration = prog_setting.parameter["current cycle"]

    while current_iteration < prog_setting.parameter["total cycle"]:
        with open(output_file, mode="a") as f:
            f.writelines(f"Test run {current_iteration}\n")
        print(f"Test run {current_iteration}")
        current_iteration += 1
        prog_setting.update_param("current cycle", current_iteration)
        save_parameter(prog_setting, "prog_data")
        input("continu")


def save_iteration_done(file_name, current_iteration):
    with open(file_name, "w") as f:
        reader = csv.reader(f)
        mydict = {rows[0]: rows[1] for rows in reader}

def save_parameter(obj, output_filename):
    with open(output_filename, "wb") as output_file:
        pickle.dump(obj, output_file)

def load_parameter(file):
    with open(file, "rb") as input_file:
        return pickle.load(input_file)

def invit_selection():
    choice = input("Continiue (C) previous session or restart new (N) one")
    if choice.upper() == "C":
        return load_parameter("prog_data")
    elif choice.upper() == "N":
        program_setting = setting_param("prog_data2.csv")
        if not path.exists(program_setting.parameter["output file name"]):
            return setting_param("prog_data2.csv")
        else:
            print("File already exist.")
            return None



def main():

    prog_setting = invit_selection()
    if prog_setting != None:

        # prog_setting = setting_param()
        save_parameter(prog_setting, "prog_data")
        test_run(prog_setting)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
