from Classes.Windows import Windows
from Classes.Line import Line
from Classes.Point import Point
from Classes.Cell import Cell

window = Windows(1000, 1000)

point_a = Point(100, 100)
point_b = Point(100, 250)
p_c = Point(200,300)
p_d = Point(350, 100)
line = Line(point_a,point_b)
line_b = Line(p_c, p_d)
cell = Cell(200,200,300,300, window)
cell2 = Cell(100,350,250,150, window)
cell3 = Cell(100,350,250,150, window)


window.draw_line(line, 'red')
window.draw_line(line_b, 'green')
cell.draw(200,200,250,150, 'blue')
cell2.draw(250,250,300,200, 'purple')
cell3.draw(300,200,350,150, 'orange')
window.wait_for_close()


