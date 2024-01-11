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
    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        top_left = Point(top_left_x, top_left_y)
        bottom_right = Point(bottom_right_x, bottom_right_y)
        top_right = Point(bottom_right_x, top_left_y)
        bottom_left = Point(top_left_x, bottom_right_y)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left), Line(bottom_left))
        if self.has_top_wall:
            self._win.draw_line(Line(top_left), Line(top_right))
        if self.has_right_wall:
            self._win.draw_line(Line(top_right), Line(bottom_right))
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_right), Line(bottom_left))
