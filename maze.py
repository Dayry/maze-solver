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
        if num_cols < 1:
            raise Exception("Must be at least one column") 
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for r in range(self._num_cols):
            col = []
            for c in range(self._num_rows):
                x1, y1, x2, y2, = self._calc_pos(self._x1, self._y1, 
                    self._cell_size_x, self._cell_size_y, r, c)
                col.append(Cell(x1, y1, x2, y2, self._win))
            self._cells.append(col)
        
        # make own method?
        if self._win:
            for col in self._cells:
                for cell in col:
                    cell.draw()
                    self._animate()


    def _calc_pos(
            self, maze_x, maze_y,
            cell_size_x, cell_size_y,
            cell_row, cell_col):
        x1 = cell_size_x * (cell_row + 1) + maze_x - cell_size_x 
        # these minuses are so dirty
        y1 = cell_size_y * (cell_col + 1) + maze_y - cell_size_y
        x2 = x1 + cell_size_x
        y2 = y1 + cell_size_y

        return x1, y1, x2, y2


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)