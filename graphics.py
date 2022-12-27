from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        """Creates new window with given dimenstions"""
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