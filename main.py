from Classes.Windows import Windows
from Classes.Line import Line
from Classes.Point import Point


window = Windows(500, 500)

point_a = Point(100, 100)
point_b = Point(100, 250)
p_c = Point(200,300)
p_d = Point(350, 100)
p_e = Point(150, 240)
p_f = Point(300, 187) 
line = Line(point_a,point_b)
line_b = Line(p_c, p_d)
line_c = Line(p_e, p_f)

window.draw_line(line, 'red')
window.draw_line(line_b, 'green')
window.draw_line(line_c, 'blue')
window.wait_for_close()


