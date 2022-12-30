from graphics import Window, Line, Point, Cell
from maze import Maze


def main():
    win = Window(800,600)

    """
    # Drawing tests
    # Line tests
    point_1 = Point(400, 450)
    point_2 = Point(200, 300)
    line_a = Line(point_1, point_2)
    win.draw_line(line_a, "black")

    # Cell tests
    cell1 = Cell(350, 300, 400, 350, win)
    cell1.draw()
    cell2 = Cell(550, 150, 600, 200, win)
    cell2.draw()
    cell3 = Cell(10, 10, 400, 300, win)
    cell3.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)"""

    rows = 10
    cols = 7
    maze = Maze(20, 20, rows, cols, 50, 50, win)
    a = maze._cells[cols-1][rows-1]
    b = maze._cells[0][0]


    win.wait_for_close()


main()
