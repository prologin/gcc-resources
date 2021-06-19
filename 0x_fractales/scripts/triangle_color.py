#!/usr/bin/python3

from turtle import *
import math

def draw_inverse_tri(x : float, y : float, length : float):
    goto(x + length, y + length)
    begin_fill()
    right(90)
    forward(length)
    right(135)
    forward(math.sqrt(length * length + length * length))
    right(135)
    forward(length)
    end_fill()

def frac_tri(x : float, y : float, length : float, b : int, r : int, increment : int):
    if length < 25:
        return
    fillcolor(r, 0, b)
    draw_inverse_tri(x, y, length / 2)

    frac_tri(x, y, length / 2, b - increment, r + increment, increment // 2)
    frac_tri(x + length / 2, y, length / 2, b + increment, r - increment, increment // 2)
    frac_tri(x, y + length / 2, length / 2, b + increment, r - increment, increment // 2)

speed(0)
penup()
colormode(255)
frac_tri(-500, -500, 1000, 255 // 2, 255 // 2, 255 // 4)

input()
