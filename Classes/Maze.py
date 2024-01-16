from Classes.Windows import Windows
from Classes.Cell import Cell

class Maze: 
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win:Windows) -> None:
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
    def _create_cells(self):
        pass