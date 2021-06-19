#!/usr/bin/python3

from turtle import *
import math

def draw_tri(x : float, y : float, length : float):
    goto(x, y)
    begin_fill()
    forward(length)
    left(135)
    forward(math.sqrt(length * length + length * length))
    left(135)
    forward(length)
    left(90)
    end_fill()

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

def frac_tri(x : float, y : float, length : float):
    if length < 25:
        return
    draw_inverse_tri(x, y, length / 2)

    frac_tri(x, y, length / 2)
    frac_tri(x + length / 2, y, length / 2)
    frac_tri(x, y + length / 2, length / 2)

speed(0)
penup()
color('black', 'black')
frac_tri(-500, -500, 1000)

input()
