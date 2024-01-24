from Classes.Windows import Window
from Classes.Cell import Cell

class Maze: 
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win:Window) -> None:
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
    def _create_cells(self):
        #this method should fill self._cells with lists of cells. 
        #Each top-level list is a column of Cell objecs. 
        #Once the matrix is populated it should call its _draw_cell metod on each Cell
        for i in range(self.num_cols):
            new_col = []
            for j in range(self.num_rows):
                pass
    def _draw_cell(self, i, j):
        #This method should calculate the x/y positoion of the Cell based on i, j, the cell_size, and the x/y position of the maze itself.
        #The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.
        #Once that's calculate, it should draw the cell and call the maze's _animate method. 
        pass
    def _animate(self):
        #The animate method is what allows us to visualize what the algorithms are doing in real time. 
        #It should simply call the window's redraw() method, then sleep for a short amount of time so your eyes keep up with each render frame. I slept for 0.05 seocnds. 
        pass