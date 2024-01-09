from tkinter import Tk, BOTH, Canvas

class Windows:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height 
        self.root = Tk()
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False

