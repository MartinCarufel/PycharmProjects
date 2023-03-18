import pandas as pd
import re
from tkinter import filedialog

def main():
    sourcefile = filedialog.askopenfilename()
    keywords = ["Meshing Time", "GPU Texture mapping enabled", "Texturing Time", "Total meshing Time"]


    with open(sourcefile, 'r') as f:
        for line in f:
            for keyword in keywords:
                if line.find(keyword) != -1:
                    print(line, end='')
                    pass



if __name__ == '__main__':
    main()

