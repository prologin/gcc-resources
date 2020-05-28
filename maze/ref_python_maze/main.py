from maze import *
from binarymaze import *
from primmaze import *


if __name__ == "__main__":
    res_maze = generate_prim_maze(4, (0, 0), (3, 3))
    print(res_maze.pretty_print())
