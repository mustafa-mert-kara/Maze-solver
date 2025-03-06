

class Line():
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def draw(self,canvas,fill_color):
        canvas.create_line(
    self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
)


class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

def find_cell_center(x1,y1,x2,y2):
    return (x1+x2)//2,(y1+y2)//2

class Cell():
    def __init__(self,window):        
        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True
        self._x1=None
        self._x2=None
        self._y1=None
        self._y2=None
        self._visited=False
        self._win=window

    def draw(self,x1,y1,x2,y2):
        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2
        if self._win is None:
            return
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"#d9d9d9")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"#d9d9d9")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"#d9d9d9")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color="gray"
        else:
            fill_color="red"
        curr_center=find_cell_center(self._x1,self._y1,self._x2,self._y2)
        target_center=find_cell_center(to_cell._x1,to_cell._y1,to_cell._x2,to_cell._y2)
        self._win.draw_line(Line(Point(curr_center[0],curr_center[1]),Point(target_center[0],target_center[1])),fill_color)
