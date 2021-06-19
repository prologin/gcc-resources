#!/usr/bin/python3

from turtle import *
import time
import math

start_time = time.time()

speed(0)
penup()
colormode(255)

def draw_line(length : float, iterations : int):
    t = 10 * (time.time() - start_time)
    mod = 255 + 255 / 2
    rx = (t % mod) * math.pi / 255
    gx = ((t + 255) % mod) * math.pi / 255
    bx = ((t + 255 / 2) % mod) * math.pi / 255
    r = (int) (255 * max(math.sin(rx), 0))
    g = (int) (255 * max(math.sin(gx), 0))
    b = (int) (255 * max(math.sin(bx), 0))

    pencolor(r, g, b)
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
r = 255
g = 0
b = 0
pencolor(r, g, b)
pendown()
draw_line(length, iterations)

input()
