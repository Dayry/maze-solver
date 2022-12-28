from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__window_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
    
    def close(self):
        self.__window_running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)


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

    def __init__(self, x1, y1, x2, y2, win):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self): #top_left_x, top_left_y, bottom_right_x, bottom_right_y
        if self.has_left_wall:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_wall, "black")
        

