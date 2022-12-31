from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        self._root = Tk()
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack()
        self._window_running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._window_running = True
        while self._window_running:
            self.redraw()
    
    def close(self):
        self._window_running = False

    def draw_line(self, line, fill_colour):
        line.draw(self._canvas, fill_colour)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_colour, width=2
        )
        canvas.pack()


class Cell:

    def __init__(self, x1, y1, x2, y2, win=None):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self): #top_left_x, top_left_y, bottom_right_x, bottom_right_y
        if self._win:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))

            if self.has_left_wall:
                self._win.draw_line(left_wall, "black")
            else:
                self._win.draw_line(left_wall, "white")
            if self.has_right_wall:
                self._win.draw_line(right_wall, "black")
            else:
                self._win.draw_line(right_wall, "white")
            if self.has_top_wall:
                self._win.draw_line(top_wall, "black")
            else:
                self._win.draw_line(top_wall, "white")
            if self.has_bottom_wall:
                self._win.draw_line(bottom_wall, "black")
            else:
                self._win.draw_line(bottom_wall, "white")

    # move (draw a line) from center of self to center of to_cell
    def draw_move(self, to_cell, undo=False):
        if self._win:
            self_mid_x = self._x1 + (self._x2 - self._x1)/2
            self_mid_y = self._y1 + (self._y2 - self._y1)/2
            to_cell_mid_x = to_cell._x1 + (to_cell._x2 - to_cell._x1)/2
            to_cell_mid_y = to_cell._y1 + (to_cell._y2 - to_cell._y1)/2
            self_center = Point(self_mid_x, self_mid_y)
            to_cell_center = Point(to_cell_mid_x, to_cell_mid_y)
            line_colour = "blue"
            if undo:
                line_colour = "red"
            movement = Line(self_center, to_cell_center)
            self._win.draw_line(movement, line_colour)

    

    

    
        

