from tkinter import Tk, BOTH, Canvas

class Windows:
    def __init__(self, width, height) -> None:
        # constructor should take a width and height
        self.width = width
        self.height = height 
        # create a new root widget using TK(), set the title property, and link our close method to the closing the window
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # create a canvas, and pack it
        self.canvas = Canvas()
        self.canvas.pack()
        # set running to False
        self.running = False
    
    def redraw(self):
        # tkinter is not 'reactive.' It needs to be told when it should re-render visuals as long at it is running
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.running = True
        # call redraw over and over while running is true
        while self.running:
            self.redraw()
    def close(self):
        # stops the redraw loop from running
        self.running = False
