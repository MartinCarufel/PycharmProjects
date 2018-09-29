#coding: utf-8

from time import sleep
from tkinter import *

name = ["Martin", "Simon", "Jean", "Eric", "Josee", "Gabriel"]

root = Tk()
root.geometry("800x800")

font_helvetica_25 = ("Helvetica", 25, "bold")
img1 = PhotoImage(file='s-l1000.png')

#can1 = Canvas(height=490, width=990, bg="coral3")
can1 = Canvas(height=800, width=800)
#lab1 = Label(text="Allo", font=font_helvetica_25)
can1.create_image(400,400,image=img1)

lab_list = [0]*8
for i in range(len(name)):
    print(i)
    #lab_list.append(name[i])
    #lab_list.append("lab{}" .format(name.index(i)))
    lab_list[i] = Label(text=name[i], font=font_helvetica_25)
    #lab_list[name.index(i)] = Label(text="i", font=font_helvetica_25)
    #print(lab_list)


x_pos = [400,650,700,650,400,150,50,150]
y_pos = [50,150,380,600,730,600,380,150]

#for x, y in zip(x_pos, y_pos):
#    lab_list[i].place(x=x, y=y, anchor=CENTER)

lab_list[0].place(x=x_pos[0], y=y_pos[0], anchor=CENTER)
lab_list[1].place(x=x_pos[1], y=y_pos[1], anchor=CENTER)
lab_list[2].place(x=x_pos[2], y=y_pos[2], anchor=CENTER)
lab_list[3].place(x=x_pos[3], y=y_pos[3], anchor=CENTER)
lab_list[4].place(x=x_pos[4], y=y_pos[4], anchor=CENTER)
lab_list[5].place(x=x_pos[5], y=y_pos[5], anchor=CENTER)
lab_list[6].place(x=x_pos[6], y=y_pos[6], anchor=CENTER)
lab_list[7].place(x=x_pos[7], y=y_pos[7], anchor=CENTER)

can1.place(height=800, width=800)

root.mainloop()
