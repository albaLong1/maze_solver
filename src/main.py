from window import Window
from cell import Cell
from maze import Maze


def main():
    win = Window(500, 500)

    maze = Maze(10,10,15,15,25,25,win)
    maze.solve()

    win.wait_for_close()


main()