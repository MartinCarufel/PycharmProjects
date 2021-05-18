from tkinter import filedialog




save_file = filedialog.asksaveasfilename()

merge_new_file = True

while merge_new_file:
    file_to_merge = filedialog.askopenfilename()
    print(file_to_merge.split("/")[-1])
    # print(file_to_merge)

    with open(save_file, 'a') as outfile:
        with open(file_to_merge) as infile:
            for line in infile:
                outfile.write(line)
    cont = input("New file to import (Y/N): ")

    if cont.upper() == 'N':
        merge_new_file = False
    else:
        merge_new_file = True