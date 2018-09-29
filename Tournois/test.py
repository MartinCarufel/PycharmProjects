# coding: utf-8

from tkinter import *


class App(Frame):
    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, width=200, height=200, **kwargs)
        self.pack()
        self.texte = Label(self, text="Allo")
        self.texte.pack()

        self.texte.place(anchor=NW, relx=0, rely=0)
        self.bouton1 = Button(self, text="New button", command= lambda: print("Bonjour"))
        self.bouton1.pack()
        self.bouton1.place(anchor=NE, relx=1, rely=0)


win1 = Tk()
app = App(win1)
app.mainloop()


