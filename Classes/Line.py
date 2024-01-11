from tkinter import Canvas

from Classes.Point import Point

class Line:
    def __init__(self, point_a:Point, point_b:Point) -> None:
        if type(point_a) != Point or type(point_b) != Point:
            raise TypeError("point_a and point_b must be of type Point")
        self.a = point_a
        self.b = point_b
    def draw(self, canvas:Canvas, fill_color='black'):
        # print(f'self.a: {self.a.x}, self.b: {self.b}')
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=3)
        canvas.pack()