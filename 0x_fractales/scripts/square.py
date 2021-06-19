#!/usr/bin/python3

from turtle import *

def draw_square(length : float):
    pendown()
    for i in range(4):
        forward(length)
        left(90)
    penup()

def frac_square(x : float, y : float, length : float, iterations):
    if iterations == 0:
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                goto(x + i * length / 3, y + j * length / 3)
                draw_square(length / 3)
            else:
                frac_square(x + i * length / 3, y + j * length / 3, length / 3, iterations - 1)

speed(0)
penup()
frac_square(-500, -500, 1000, 5)

input()
