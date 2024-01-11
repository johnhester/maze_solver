from Classes.Windows import Windows
from Classes.Line import Line
from Classes.Point import Point


window = Windows(500, 500)

point_a = Point(100, 100)
point_b = Point(100, 250)
p_c = Point(200,300)
p_d = Point(350, 100)
line = Line(point_a,point_b)
line_b = Line(p_c, p_d)


window.draw_line(line, 'red')
window.draw_line(line_b, 'green')
window.wait_for_close()


