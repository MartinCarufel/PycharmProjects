#coding:utf-8

from math import ceil
from random import shuffle
from tkinter import *
import time
import winsound
from threading import Thread


# class Alarm(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#
#     def play_alarm(self):
#         winsound.PlaySound('426408__greek555__wake-me-up.wav', winsound.SND_FILENAME)

class Alarm():
    def __init__(self):
        pass

    def play_alarm(self):
        winsound.PlaySound('426408__greek555__wake-me-up.wav', winsound.SND_FILENAME)



class Player:
    def __init__(self):
        self._ent1 = ""
        self.p_list = []
        self.table_l = []
        self.table = []
        self.remain_item = []

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
            self.tx.insert(END, i+"\n")

        # print("Button affiche: {}".format(tx_aff.get()))
        # print(ent1.get())
        #but2 = Button(win1, text=tx_aff.get(), command=lambda: edit_player(name.get()))
        #but2.pack()
        #print(type(but2))
        #print(self.p_list)

    def del_all_text(self):
            self.tx.delete('1.0', END)
            self.p_list = []

    def create_table(self):
        shuffle(player.p_list)
        #print(player.p_list)
        d_copy = list(player.p_list)
        nb_par_table = int(app.ent2.get())
        #print(nb_par_table)


        table = {"table" + str(i + 1): "" for i in range(ceil(len(player.p_list) / nb_par_table))}
        table_list = table.keys()
        table_l = []
        for i in table_list:
            table_l.append(i)

        # print(type(table_list))

        for i in range(len(table_l)):
            start = i * len(player.p_list) // len(table)
            end = (i * len(player.p_list) // len(table)) + len(player.p_list) // len(table)
            dx = player.p_list[start:end]
            temp = {table_l[i]: dx}
            table.update(temp)
            remain_item = list(set(d_copy).difference(set(dx)))
            d_copy = list(remain_item)

        for i in range(len(remain_item)):
            # add_value = "{}".format(table.get(table_l[i])) + remain_item[i]
            add_value = list(table.get(table_l[i]))
            add_value.append(remain_item[i])
            temp = {table_l[i]: add_value}
            table.update(temp)

        #print(table_l)
        #print(table)
        #print(remain_item)

        app.tx.delete(1.0, END)
        for i, j in table.items():
            app.tx.insert(END, i + "\n")
            app.tx.insert(END, j)
            app.tx.insert(END,  " \n\n")


class MyTymer:
    def __init__(self):
        pass

    @classmethod
    def start_timer(self, xtime):
        self.pause = False
        self.alarm_on = True
        #xtime = int(xtime.get())
        for t in range(xtime, -1, -1):
            time_remain = t
            if self.pause:
                break
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            app.time_str.set(sf)
            app.but4.config(state=DISABLED)
            win1.update()
            # delay one second
            time.sleep(1)

        if time_remain == 0:
            for i in range(1):
           #winsound.PlaySound('426408__greek555__wake-me-up.wav',winsound.SND_FILENAME)
                al_1 = Alarm()
                #al_1.start()
                al_1.play_alarm()
                app.but4.config(state=NORMAL)
                #stop_alarm = input()
                #if stop_alarm != "":
                    #break


    @classmethod
    def pause_timer(self):
        self.hold_timer = int(app.time_str.get()[0:2]) * 60 + int(app.time_str.get()[3:6])
        #print(self.hold_timer)
        self.pause = True


    @classmethod
    def resume_timer(self):
        self.pause = False
        MyTymer.start_timer(self.hold_timer)
        # for t in range(self.hold_timer, -1, -1):
        #     if self.pause:
        #         break
        #     sf = "{:02d}:{:02d}".format(*divmod(t, 60))
        #     app.time_str.set(sf)
        #     win1.update()
        #     # delay one second
        #     time.sleep(1)


# class Stop_alarm(Frame):
#     def __init__(self, win2, **kwargs):
#         Frame.__init__(self, **kwargs)
#         self.time_str = StringVar()
#         self.label_font = ('helvetica', 60)
#         self.tx = Text(win2)


class App(Frame):
    def __init__(self, win1, **kwargs):
        Frame.__init__(self, **kwargs)
        self.time_str = StringVar()
        self.label_font = ('helvetica', 160)
        self.tx = Text(win1)

        self.tx.grid(row=4, column=0, columnspan=4)

        self.ent1 = Entry()
        self.ent2 = Entry()
        self.ent3 = Entry()

        lab1 = Label(win1, text="Name")
        lab2 = Label(win1, text="Nb player per table")
        lab3 = Label(win1, textvariable=self.time_str, font=self.label_font, bg='white',
                     fg='blue', relief='raised', bd=3)

        but1 = Button(win1, text="Add player", command=lambda: player.add_player(self.tx, self.ent1))
        but2 = Button(win1, text="Delete all", command=lambda: player.del_all_text())
        but3 = Button(win1, text="Create Table", command=lambda: player.create_table())
        self.but4 = Button(win1, text="Start", command=lambda: MyTymer.start_timer(int(self.ent3.get())*1))
        #but4 = Button(win1, text="Start", command=lambda: MyTymer.start_timer(1800))
        but5 = Button(win1, text="Pause", command=lambda: MyTymer.pause_timer())
        but6 = Button(win1, text="Resume", command=lambda: MyTymer.resume_timer())

        lab1.grid(row=0, column=0, stick=E)
        lab2.grid(row=3, column=0, sticky=E)
        #lab3.grid(row=5, rowspan=3, padx=5, pady=5)
        lab3.grid(row=1, column=4, rowspan=4, columnspan=4, padx=5, pady=5)

        but1.grid(row=0, column=2, padx=5, sticky=W)
        but2.grid(row=0, column=3, rowspan=4, padx=10, ipady=10, ipadx=20, sticky=W)
        but3.grid(row=3, column=2, sticky=W)
        self.but4.grid(row=5, column=5)
        but5.grid(row=5, column=6)
        but6.grid(row=5, column=7)

        self.ent1.grid(row=0, column=1, padx=5, sticky=W)
        self.ent2.grid(row=3, column=1, padx=5, sticky=W)
        self.ent3.grid(row=5, column=4)

        #print("loop")

player = Player()
xtimer = MyTymer()
win1 = Tk()
app = App(win1)
win1.mainloop()

#table_list[0] = "allo"
# print(Player.table_l)
# print(Player.table)
# print(Player.remain_item)
