#coding:utf-8

import turtle

x = turtle.Turtle()

seg = 16
angle = int(180/seg)
for i in range(int(seg*2)):
    x.forward(200)
    x.left(180-angle)

turtle.done()
