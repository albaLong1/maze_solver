from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        
        # Initialize the Canvas with the root, and set width and height
        self.canvas = Canvas(self.root, width=width, height=height)
        
        # Pack the Canvas so it appears in the window
        self.canvas.pack()
        
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self,line,fill_color="black"):
        line.draw(self.canvas,fill_color)


class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        
class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        
    def draw(self,canvas, fill_color="black"):
        canvas.create_line(self.p1.x_coordinate, self.p1.y_coordinate, self.p2.x_coordinate, self.p2.y_coordinate, fill=fill_color, width=2)



    