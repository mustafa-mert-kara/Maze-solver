
from window_objects import Cell
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1=x1
        self._y1=y1
        self._num_rows=num_rows
        self._num_cols=num_cols
        self._cell_size_x=cell_size_x
        self._cell_size_y=cell_size_y
        self._win=win
        self._cells=[]

        if seed is not None:
            random.seed(seed)

        self.create_cells()

        self._break_entrance_and_exit()

        self._break_walls_r(0,0)

        self._reset_cells_visited()
    
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell._visited=False
    
    
    def is_in_confineds(self,x,y):
        return x>=0 and y>=0 and x<self._num_rows and y < self._num_cols
    def has_wall(self,row1,col1,row2,col2):
        if row1<row2:
            return self._cells[row1][col1].has_bottom_wall
        elif row1>row2:
            return self._cells[row1][col1].has_top_wall
        elif col1<col2:
            # print("col1<col2")
            # print(self._cells[row1][col1].has_right_wall)
            return self._cells[row1][col1].has_right_wall
        else:
            # print("col1>col2")
            # print(self._cells[row1][col1].has_right_wall)
            return self._cells[row1][col1].has_left_wall
    
    def _break_walls(self,row1,col1,row2,col2):
        if row1<row2:
            self._cells[row1][col1].has_bottom_wall=False
            self._cells[row2][col2].has_top_wall=False
        elif row1>row2:
            self._cells[row1][col1].has_top_wall=False
            self._cells[row2][col2].has_bottom_wall=False
        elif col1<col2:
            self._cells[row1][col1].has_right_wall=False
            self._cells[row2][col2].has_left_wall=False
        else:
            self._cells[row1][col1].has_left_wall=False
            self._cells[row2][col2].has_right_wall=False

    def _break_walls_r(self, row, col):
        self._cells[row][col]._visited=True
        while True:
            to_visit=[]
            for x,y in [[0,-1],[0,1],[-1,0],[1,0]]:
                if self.is_in_confineds(row+x,col+y) and not self._cells[row+x][col+y]._visited:
                    to_visit.append([row+x,col+y])
            if len(to_visit)==0:
                self._draw_cell(row,col)
                return
            direction=random.randint(0,len(to_visit)-1)
            self._break_walls(row,col,to_visit[direction][0],to_visit[direction][1])
            self._break_walls_r(to_visit[direction][0],to_visit[direction][1])


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall=False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall=False
        self._draw_cell(self._num_rows-1,self._num_cols-1)

    def create_cells(self):
        for i in range(self._num_rows):
            rows=[]
            for j in range(self._num_cols):
                rows.append(Cell(self._win))                
            self._cells.append(rows)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)
    def _draw_cell(self,row,col):
        base_shift=10
        self._cells[row][col].draw(col*self._cell_size_x+base_shift,row*self._cell_size_y+base_shift,(col+1)*self._cell_size_x+base_shift,(row+1)*self._cell_size_y+base_shift)
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        # time.sleep(0.05)

    def solve_r(self,i,j):
        print("in cell",i,j)
        self._animate()
        self._cells[i][j]._visited=True
        if i==self._num_rows-1 and j==self._num_cols-1:
            return True
        for x,y in [[0,-1],[0,1],[-1,0],[1,0]]:
            if self.is_in_confineds(i+x,y+j) and not self.has_wall(i,j,i+x,j+y)  and not self._cells[i+x][y+j]._visited:
                self._cells[i][j].draw_move(self._cells[i+x][y+j],False)
                res=self.solve_r(i+x,y+j)
                if res:
                    return res
                self._cells[i][j].draw_move(self._cells[i+x][y+j],True)
        return False
