#!/usr/bin/python3

from turtle import *
import math

speed(0)
penup()
colormode(255)

def draw_line(length : float, iterations : int):
    if iterations == 0:
        forward(length)
    else:
        new_length = length / (2 + math.sqrt(2))
        draw_line(new_length, iterations - 1)
        left(45)
        draw_line(new_length, iterations - 1)
        right(90)
        draw_line(new_length, iterations - 1)
        left(45)
        draw_line(new_length, iterations - 1)

def pentagon(length : float, iterations : int):
    for i in range(5):
        draw_line(length, iterations)
        right(72)

length = 500
iterations = 3

goto( -length / 2, length * 0.68891909)
pendown()
pentagon(length, iterations)

input()
