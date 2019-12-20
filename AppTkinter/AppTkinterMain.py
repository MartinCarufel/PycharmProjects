# coding: utf-8

from tkinter import *


class Myclass(Tk):
    """Class defining ... """

    def __init__(self):
        """Class constructor"""
        Tk.__init__(self)
        self.geometry('300x300')
        self.frame = Frame(self)
        self.frame.pack()
        self.var = StringVar()
        self.label = Label(self.frame, text="Faite votre choix")
        self.label.grid(row=1, column=1, sticky=E)
        self.radio1= Radiobutton(self.frame, text="Choix 1", value="Choix 1", variable=self.var, command=lambda: self.getselection())
        self.radio1.grid(row=2, column=2)
        self.radio2 = Radiobutton(self.frame, text="Choix 2", value="", variable=self.var, command=lambda: self.getselection())
        self.radio2.grid(row=3, column=2)


    def getselection(self):
        """Method that do something"""
        return self.var
        print('allo')



app = Myclass()
app.mainloop()


print(app)