import time, random
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
            win=None,
            seed=None):
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

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls()

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
    
    """ Helper method for _create_cells """
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

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    """ 
    Create a path starting from every cell until no more paths can be made
    """
    def _break_walls(self):
        for col in range(self._num_cols):
            for cell in range(self._num_rows):
                self._break_walls_r(col, cell)
                

    """ Helper method for _break_walls """
    def _break_walls_r(self, x, y): # x is col, y is index in given col
        self._cells[x][y].visited = True
        possible_paths = []
        for adjacent in self._find_adjacent_cells(x, y):
            if adjacent is not None:
                if self._cells[adjacent[0]][adjacent[1]].visited == False:
                    possible_paths.append(adjacent)
        
        if len(possible_paths) < 1:
            self._cells[x][y].draw()
            return
        else:
            rand = random.randint(0, len(possible_paths)-1)
            next_x = possible_paths[rand][0]
            next_y = possible_paths[rand][1]
            next_pos = possible_paths[rand][2]
            
            self._draw_wall_break(x, y, next_x, next_y, next_pos)
            self._break_walls_r(next_x, next_y)       

    """ Helper method for _break_walls_r """
    def _draw_wall_break(self, x, y, next_x, next_y, next_pos):
        if next_pos == 0: # next cell is above
            self._cells[x][y].has_top_wall = False
            self._cells[x][y].draw()
            self._cells[next_x][next_y].has_bottom_wall = False
            self._cells[next_x][next_y].draw()
        if next_pos == 1: # next cell is below
            self._cells[x][y].has_bottom_wall = False
            self._cells[x][y].draw()
            self._cells[next_x][next_y].has_top_wall = False
            self._cells[next_x][next_y].draw()
        if next_pos == 2: # next cell is left
            self._cells[x][y].has_left_wall = False
            self._cells[x][y].draw()
            self._cells[next_x][next_y].has_right_wall = False
            self._cells[next_x][next_y].draw()
        if next_pos == 3: # next cell is right
            self._cells[x][y].has_right_wall = False
            self._cells[x][y].draw()
            self._cells[next_x][next_y].has_left_wall = False
            self._cells[next_x][next_y].draw()

    """ Helper method for _break_walls_r """
    def _find_adjacent_cells(self, x, y):
        adjacent_cells = [None, None, None, None]
        if y - 1 >= 0: # top
            adjacent_cells[0] = [x, y-1, 0]
        if y + 1 < self._num_rows: # bottom
            adjacent_cells[1] = [x, y+1, 1]
        if x - 1 >= 0: # left
            adjacent_cells[2] = [x-1, y, 2]
        if x + 1 < self._num_cols: # right
            adjacent_cells[3] = [x+1, y, 3]
        
        return adjacent_cells