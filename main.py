from Classes.Windows import Window
from Classes.Line import Line
from Classes.Point import Point
from Classes.Cell import Cell

window = Window(1000, 1000)

point_a = Point(100, 100)
point_b = Point(100, 250)
p_c = Point(200,300)
p_d = Point(350, 100)
p_e = Point(150, 240)
p_f = Point(300, 187) 
line = Line(point_a,point_b)
line_b = Line(p_c, p_d)
cell = Cell(window)
cell2 = Cell(window)
cell3 = Cell(window)


cell.draw(200,200,250,150,'blue')
cell2.draw(250,250,300,200, 'purple')
cell3.draw(300,200,350,150, 'orange')
cell.draw_move(cell3)
cell3.draw_move(cell2)
window.wait_for_close()


