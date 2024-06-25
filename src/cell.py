from window import Window, Point, Line 
class Cell():
    def __init__(self,_win):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = _win
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_left_wall = True
    
    def draw(self,x1,y1,x2,y2):
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x2,y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x1,y1),Point(x2,y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1,y1),Point(x2,y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y2))
            self._win.draw_line(line)
    
    def draw_move(self,to_cell, undo=False):
        if undo == False:
            fill_color= "red"
        else:
            fill_color = "gray"
        