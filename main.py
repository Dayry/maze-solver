from graphics import Window, Line, Point


def main():
    win = Window(800,600)

    # Line tests
    point_1 = Point(400, 450)
    point_2 = Point(200, 300)
    line_a = Line(point_1, point_2)
    win.draw_line(line_a, "black")

    win.wait_for_close()


main()
