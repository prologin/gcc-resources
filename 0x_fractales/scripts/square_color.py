#!/usr/bin/python3

from turtle import *

def draw_square(length : float):
    begin_fill()
    for i in range(4):
        forward(length)
        left(90)
    end_fill()

def frac_square(x : float, y : float, length : float, iterations, r, g, b, increment):
    if iterations == 0:
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                goto(x + i * length / 3, y + j * length / 3)
                fillcolor(r, g, b)
                draw_square(length / 3)
            else:
                new_r = max(0, r + (i - 1) * increment - j * increment // 4)
                new_g = min(255, g + 2 * j * increment)
                new_b = max(0, b - (i - 1) * increment - j * increment // 4)
                frac_square(x + i * length / 3, y + j * length / 3, length / 3, iterations - 1, new_r, new_g, new_b, increment // 2 - increment // 10)

speed(0)
penup()
colormode(255)
fillcolor(0, 0, 0)
frac_square(-500, -500, 1000, 4, 255 // 2, 0, 255 // 2, 255 // 4)

input()
