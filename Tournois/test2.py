# coding: utf-8

from tkinter import *


class Player:
    def __init__(self):
        self._ent1 = ""
        self.p_list = []

    def _get_ent1(self):
        return self._ent1

    def _set_ent1(self, new):
        #print("Add player")
        self._ent1 = new

    ent1 = property(_get_ent1, _set_ent1)

    def edit_player(self, p_name=""):
        win2 = Tk()
        win2.title(p_name)
        lab = Label(win2, text=p_name)
        lab.pack()

    def add_player(self, tx, name):
        """Class constructor"""
        self.tx = tx
        self.p_list.append(name.get())

        #tx.insert(END, name.get()+"\n")
        tx.delete(1.0,END)
        for i in self.p_list:
            tx.insert(END, i+"\n")

        # print("Button affiche: {}".format(tx_aff.get()))
        # print(ent1.get())
        #but2 = Button(win1, text=tx_aff.get(), command=lambda: edit_player(name.get()))
        #but2.pack()
        #print(type(but2))
        #print(self.p_list)

class App(Frame):
    def __init__(self, win1, **kwargs):
        Frame.__init__(self, **kwargs)

        ent1 = Entry()
        tx = Text(win1)

        but1 = Button(win1, text="Add player", command=lambda: player.add_player(tx, ent1))
        ent1.pack()
        but1.pack()
        tx.pack()
        #print("loop")


player = Player()

win1 = Tk()
app = App(win1)
win1.mainloop()


