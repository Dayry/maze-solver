from graphics import Window, Line, Point, Cell


def main():
    win = Window(800,600)

    """# Line tests
    point_1 = Point(400, 450)
    point_2 = Point(200, 300)
    line_a = Line(point_1, point_2)
    win.draw_line(line_a, "black")"""

    # Cell tests
    cell = Cell(400, 200, 450, 300, win)
    cell.has_bottom_wall = False
    cell.has_right_wall = False
    cell.has_left_wall = False
    cell.draw()

    win.wait_for_close()


main()
