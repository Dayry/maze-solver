import time
from graphics import Cell

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self.__create_cells()

    def __create_cells(self):
        for r in range(self.__num_cols):
            col = []
            for c in range(self.__num_rows):
                x1, y1, x2, y2, = self.__calc_pos(self.__x1, self.__y1, 
                    self.__cell_size_x, self.__cell_size_y, r, c)
                col.append(Cell(x1, y1, x2, y2, self.__win))
            self.__cells.append(col)
        
        for col in self.__cells:
            for cell in col:
                cell.draw()
                self.__animate()


    def __calc_pos(
            self, maze_x, maze_y,
            cell_size_x, cell_size_y,
            cell_row, cell_col):
        x1 = cell_size_x * (cell_row + 1) + maze_x - cell_size_x 
        # these minuses are so dirty
        y1 = cell_size_y * (cell_col + 1) + maze_y - cell_size_y
        x2 = x1 + cell_size_x
        y2 = y1 + cell_size_y

        return x1, y1, x2, y2


    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)