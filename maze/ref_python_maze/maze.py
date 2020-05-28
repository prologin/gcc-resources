from enum import Enum

class Cell:
    up = True
    down = True
    left = True
    right = True
    start = False
    end = False
    is_path = False

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
        stars = "=="
        for i in range(self.size):
            stars += "======"

        res = stars + "\n"
        for i in range(self.size):
            first_line = "||"
            third_line = "=="
            for j in range(self.size):
                if self.maze[i][j].start:
                    first_line += "SSSS"
                elif self.maze[i][j].end:
                    first_line += "EEEE"
                elif self.maze[i][j].is_path:
                    first_line += "PPPP"
                else:
                    first_line += "    "

                if self.maze[i][j].right:
                    first_line += "||"
                elif self.maze[i][j].is_path and self.maze[i][j + 1].is_path:
                    first_line += "PP"
                else:
                    first_line += "  "

                if self.maze[i][j].down:
                    third_line += "======"
                elif self.maze[i][j].is_path and self.maze[i + 1][j].is_path:
                    third_line += "PPPP"
                else:
                    third_line += "    "
                    third_line += "=="

            first_line += "\n"
            third_line += "\n"
            res += first_line + first_line + third_line

        return res

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
