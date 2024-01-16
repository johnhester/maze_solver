from Classes.Windows import Windows
from Classes.Line import Line
from Classes.Point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win:Windows, left_wall = True, right_wall = True, top_wall = True, bottom_wall = True) -> None:
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall 
        self.has_bottom_wall = bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    def draw(self, fill_color):
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left), fill_color)
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), fill_color)
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right), fill_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_right, bottom_left), fill_color)
    def draw_move(self, to_cell, undo=False):
        line_color = 'red'
        if undo:
            line_color = 'gray'

        width = self._x2 - self._x1
        height = self._y1 - self._y2
        self_center = Point((self._x1 + width//2),(self._y2 + height//2))
        to_cell_width = to_cell._x2 - to_cell._x1
        to_cell_height = to_cell._y1 - to_cell._y2
        to_cell_center = Point((to_cell._x1 + to_cell_width//2), (to_cell._y2 + to_cell_height//2))
        # draw line
        self._win.draw_line(Line(self_center, to_cell_center), line_color)