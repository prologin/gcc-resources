from random import random
from maze import *


def get_directions(i, j):
    all_dir = []
    if i - 1 >= 0:
        all_dir.append(Direction.NORTH)
    if j - 1 >= 0:
        all_dir.append(Direction.WEST)
    return all_dir


def generate_binary_maze(size, start, end):
    res_maze = Maze(size, start, end)
    for i in range(size, 0, -1):
        for j in range(size, 0, -1):
            all_dir = get_directions(i, j)
            if len(all_dir) != 0:
                index = random.randrange(len(all_dir))
                res_maze.carve_path(i, j, index)
    return res_maze
