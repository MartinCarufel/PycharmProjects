# coding: utf-8


from tkinter import *
from PIL import Image, ImageTk

fen = Tk()
fen.geometry('1000x1000')
w = Canvas(fen,width=700, height=700)
w.place(relx=0.5, rely=0.5, anchor=CENTER)
image = Image.open("s-l1000.jpg")
photo = ImageTk.PhotoImage(image)
image = w.create_image(0, 0, anchor=NW, image=photo)

overlay = Canvas(fen,width=50, height=50)
overlay.place(x=100, y=100, anchor=CENTER)
gmail = Image.open("gmail.jpg")
photo2 = ImageTk.PhotoImage(gmail)
image = overlay.create_image(0, 0, anchor=NW, image=photo2)

table = Canvas(fen, width=482, height=482, borderwidth=0)
points = [142, 2, 342, 2, 482, 142, 482, 342, 342, 482, 142, 482, 2, 342, 2, 142]
table.create_polygon(points, outline='#f11', fill='chartreuse4', width=1)
table.place(relx=0.5, rely=0.5, anchor=CENTER)

c1 = Canvas(fen)
c1.place(x=0, y=0, anchor=NW)
dessin = Image.open("table_poker.png")
photo3 = ImageTk.PhotoImage(dessin)
image = c1.create_image(0, 0, anchor=NW, image=photo3)



dessin = c1.create_image((0, 0, ))
image = Image.open("s-l1000.jpg")
fen.mainloop()
