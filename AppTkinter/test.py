# coding: utf-8
from tkinter import *

list = ['454033065745', 'Achat ici', '16.50', 'none']


def getselection(var):
    """Method that do something"""
    list[3] = var.get()
    print(list)
    #return var


app = Tk()
app.geometry('300x300')
frame = Frame(app)
frame.pack()
var = StringVar(value='choix 1')
label = Label(frame, text="Faite votre choix")
label.grid(row=1, column=1, sticky=E)
radio1= Radiobutton(frame, text="Choix 1", value="Choix 1", variable=var, command=lambda: getselection(var))
radio1.grid(row=2, column=2)
radio2 = Radiobutton(frame, text="Choix 2", value="Choix 2", variable=var, command=lambda: getselection(var))
radio2.grid(row=3, column=2)

app.mainloop()