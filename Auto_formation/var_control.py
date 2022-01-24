# coding: utf-8

from time import sleep
import tkinter
from tkinter.font import Font

app = tkinter.Tk()
app.geometry("400x300")
app.title("Compteur")


myFont = Font(family="Times", size=240, weight="bold")
labelNum = tkinter.StringVar()
label = tkinter.Label(app, font=myFont, textvariable=labelNum)
label.pack()


for x in range(20, -1, -1):
    labelNum.set(x)
    app.update()
    sleep(1)


app.mainloop()