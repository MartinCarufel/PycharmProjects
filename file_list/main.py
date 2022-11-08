import re
import os
from tkinter import filedialog

path = filedialog.askdirectory()
print(path)
# print(os.listdir(path))
target = filedialog.asksaveasfilename()
with open(target, mode='a') as tf:
    for file in os.listdir(path):
        tf.writelines(path + "/" + file + "\n")

