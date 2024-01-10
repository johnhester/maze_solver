from Classes.Windows import Windows
from Classes.Line import Line
from Classes.Point import Point


window = Windows(500, 500)

point_a = Point(100, 100)
point_b = Point(100, 250)
line = Line(point_a,point_b)


window.wait_for_close()
window.draw_line(line, 'blue')

