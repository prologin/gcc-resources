#!/usr/bin/python3

from turtle import *

speed(0)
penup()
colormode(255)
tracer(100000, 0)
hideturtle()

def tree(length : float, iterations : int, r : int, g : int, b : int):
    color(r, g, b)
    nr = max(0, r - r // 10)
    ng = min(255, g + 5 * g // 10)
    width(iterations // 2)
    pendown()
    forward(2 * length / 5)
    penup()

    if iterations != 0:
        left(80)
        tree(length / 4, int(0.6 * iterations), nr // 2, min(255, 2 * ng), b)
        left(100)

    width(iterations // 2)
    color(r, g, b)
    pendown()
    forward(length / 10)
    penup()

    if iterations != 0:
        right(70)
        tree(length / 6, int(0.4 * iterations), nr // 2, min(255, 2 * ng), b)
        right(110)

    width(iterations // 2)
    color(r, g, b)
    pendown()
    forward(3 * length / 10)
    penup()

    if iterations != 0:

        left(60)
        tree(length / 2, iterations - 1, nr, ng, b)
        left(120)

        color(r, g, b)
        width(iterations // 2)
        pendown()
        forward(length / 5)
        penup()

        left(10)
        tree(2.5 * length / 3, iterations - 1, nr, ng, b)
        left(125)
        tree(1.9 * length / 3, iterations - 1, nr, ng, b)
        left(45)

        forward(length)
    else:
        right(180)
        forward(4 * length / 5)


left(90)
goto(0, -400)
tree(200, 9, 135, 10, 10)

input()
