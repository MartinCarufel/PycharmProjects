# coding: utf-8

from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def get_average(path_file):
    df = pd.read_table(path_file, skiprows=10)
    avg = df["LAeq (dBA)"].mean()
    file_name = path_file.name.split("/")[-1]
    print(file_name)
    print("Average SPL:", avg)

    return (file_name, avg)

def get_continue():
    while True:
        response = input("Do you want to do another file (Y/N): ").upper()

        if response == 'Y':
            return True
        elif response == 'N':
            return False
        else:
            print("Please make sure to answer only by Y/N")

def main():
    cont = True
    file_name_list = []
    avg_list = []

    # file_name_list = ["file 1", "file 2", "file 3"]
    # avg_list = [67.45, 70.5, 68.9]

    while cont:
        path_file = filedialog.askopenfile()
        file_name, avg = get_average(path_file)
        file_name_list.append(file_name)
        avg_list.append(avg)
        cont = get_continue()



    summary_table = pd.DataFrame({"File Name":file_name_list, "Average":avg_list})
    summary_table.to_csv("Summary.csv")
    summary_table.plot.bar()
    plt.title("Sound Pressure Level Slow ")
    plt.ylabel("dBA")
    plt.show()


if __name__ == '__main__':
    """
        This program calculate dthe avrage of all record sound pressure level. The file format is a tab speparated format 
        as exported by Android app Sound Analyser app by Dominique Rodrigues
        """
    main()
