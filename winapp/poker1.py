# coding: utf-8

from tkinter import *
from PIL import Image, ImageTk
from time import sleep

player = ['Martin', 'Justin', 'Gabriel', 'Anne-Marie', 'Sebastien', 'Jean-Pierre', 'Marc-andre lepine', 'Simon']
label_pos = [(300, 100), (450, 150), (475, 300), (450, 450), (300, 500), (150, 450), (100, 300), (150, 150)]



fen = Tk()
fen.geometry('600x600')
c1 = Canvas(fen, width=600, height=600)
c1.place(x=0, y=0, anchor=NW)
dessin = Image.open("table_poker_L.png")
photo3 = ImageTk.PhotoImage(dessin)
image = c1.create_image(0, 0, anchor=NW, image=photo3)


for i in range(len(player)):
    label1 = Label(fen, text=player[i])
    label1.place(x=label_pos[i][0], y=label_pos[i][1], anchor=CENTER)

fen.mainloop()


