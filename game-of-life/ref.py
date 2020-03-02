#!/bin/env python3

ALIVE = True
DEAD = False

from os import system
from random import randint
import sys
import time

class Cell:
    def __init__(self, alive=DEAD):
        self.alive = alive
        self.char = 'O' if self.alive else '.'

    def set(self, status):
        self.alive = status
        if status == DEAD:
            self.char = '.'
        else:
            self.char = 'O'

class Board:
    def __init__(self, path, width = 0, height = 0, count = 0):
        if path is not None:
            with open(path) as f:
                pattern = f.readlines()
                for i in range(len(pattern)):
                    pattern[i] = pattern[i][:-1]

            self.width = len(pattern[0])
            self.height = len(pattern)
            self.grid = [[Cell(DEAD) for i in range(self.width)] for j in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    if pattern[i][j] != '.':
                        self.grid[i][j].set(ALIVE)

        else:
            self.width = width
            self.height = height
            self.grid = [[Cell(DEAD) for i in range(width)] for j in range(height)]
            self.seed_life(count)

    def count_neighbours(self, x, y):
        neighbours = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) \
                or (x + i < 0 or x + i >= self.height) \
                or (y + j < 0 or y + j >= self.width):
                    continue
                if self.grid[x + i][y + j].alive:
                    neighbours += 1

        return neighbours

    def seed_life(self, count):
        for c in range(count):
            x = randint(0, self.height - 1)
            y = randint(0, self.width - 1)
            while self.grid[x][y].alive:
                x = randint(0, self.height - 1)
                y = randint(0, self.width - 1)

            self.grid[x][y].set(ALIVE)

    def set_cell(self, i, j, status):
        self.grid[i][j].set(status)

    def next_generation(self):
        new_gen = [[Cell(DEAD) for i in range(self.width)] for j in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                neighbours = self.count_neighbours(i, j)
                if self.grid[i][j].alive and (neighbours < 2 or neighbours > 3):
                    new_gen[i][j].set(DEAD)
                elif neighbours == 3:
                    new_gen[i][j].set(ALIVE)
                else:
                    new_gen[i][j] = self.grid[i][j]

        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = new_gen[i][j]

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j].char, end="")
            print()
        print()

    def is_empty(self):
        for line in self.grid:
            for cell in line:
                if cell.alive:
                    return False

        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <generations> [path]")

    generations = int(sys.argv[1])
    if len(sys.argv) == 3:
        path = sys.argv[2]
        board = Board(path)
    else:
        board = Board(None, 69, 69, 120)

    i = 0
    while i < generations and not board.is_empty():
        system("clear")
        board.display()
        print(f">> Generation {i} <<")
        time.sleep(0.2)
        board.next_generation()
        i += 1
