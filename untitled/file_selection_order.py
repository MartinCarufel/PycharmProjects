# coding: utf-8

from tkinter import filedialog

def main():
    print("Hello world")
    path_file = filedialog.askopenfiles()
    # print(path_file)
    for i in path_file:
        f_name = i.name.split("/")[-1]
        print(f_name + " : " + i.mode)
        # print(i.mode)
        # print(i.name)
        pass
    # print(path_file)

if __name__ == '__main__':
    main()
