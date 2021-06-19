#!/usr/bin/python3

from turtle import *

speed(0)
penup()
colormode(255)

def draw_line(length : float, iterations : int):
    if iterations == 0:
        forward(length)
    else:
        draw_line(length / 3, iterations - 1)
        left(90)
        draw_line(length / 3, iterations - 1)
        right(90)
        draw_line(length / 3, iterations - 1)
        right(90)
        draw_line(length / 3, iterations - 1)
        left(90)
        draw_line(length / 3, iterations - 1)

goto(-500, 0)
length = 1000
iterations = 5
r = 0
g = 0
b = 0
pencolor(r, g, b)
pendown()
draw_line(length, iterations)
penup()

input()
