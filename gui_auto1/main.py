# coding: utf-8

from tkinter import *
from time import sleep
from pyautogui import *


root = Tk()
var = StringVar()
posx = 0
posy = 0
var.set('Pos X : {}, Pos Y : {}' .format(posx, posy))

l = Label(root, textvariable = var)
l.pack()

while(True):
    #sleep(1) # Need this to slow the changes down
    posx, posy = position()
    var.set('Pos X : {}, Pos Y : {}' .format(posx, posy))
    root.update_idletasks()