import re
import os
from tkinter import filedialog
import re

path = filedialog.askdirectory()
print(path)
# print(os.listdir(path))
target = filedialog.asksaveasfilename()
pattern = "\.log"
with open(target, mode='a') as tf:
    for file in os.listdir(path):
        if re.search(pattern, file) != None:
            tf.writelines(path + "/" + file + "\n")

