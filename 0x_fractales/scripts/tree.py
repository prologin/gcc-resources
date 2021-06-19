#!/usr/bin/python3

from turtle import *

speed(0)
penup()
colormode(255)
tracer(250, 0)

def tree(length : float, iterations : int, r : int, g : int, b : int):
    color(r, g, b)
    r = max(0, r - r // 10)
    g = min(255, g + 5 * g // 10)
    width(iterations // 2)
    pendown()
    forward(length)
    penup()
    if iterations != 0:
        left(35)
        tree(2 * length / 3, iterations - 1, r, g, b)
        left(120)
        tree(2.5 * length / 3, iterations - 1, r, g, b)
        left(25)
        forward(length)
    else:
        right(180)
        forward(length)


left(90)
goto(0, -400)
tree(250, 15, 135, 10, 10)

input()
