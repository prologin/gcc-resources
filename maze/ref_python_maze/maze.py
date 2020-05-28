from enum import Enum

class Cell:
    up = True
    down = True
    left = True
    right = True
    start = False
    end = False

    def __init__(self, start=False, end=False):
        self.start = start
        self.end = end


class Direction(Enum):
    NULLDIR = 0
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


class Maze:
    maze = []
    size = 0

    def __init__(self, size, start, end):
        self.size = size
        for i in range(size):
            line = []
            for j in range(size):
                cell = Cell()
                line.append(cell)
            self.maze.append(line)
        self.maze[start[0]][start[1]].start = True
        self.maze[end[0]][end[1]].end = True

    def pretty_print(self):
        pass

    def carve_path(self, i, j, direction):
        if direction == Direction.NORTH:
            self.maze[i][j].up = False
            self.maze[i - 1][j].down = False
        elif direction == Direction.SOUTH:
            self.maze[i][j].down = False
            self.maze[i + 1][j].up = False
        elif direction == Direction.EAST:
            self.maze[i][j].right = False
            self.maze[i][j + 1].left = False
        elif direction == Direction.WEST:
            self.maze[i][j].left = False
            self.maze[i][j - 1].right = False
