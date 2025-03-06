
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


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall=False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall=False
        self._draw_cell(self._num_rows-1,self._num_cols-1)

    def create_cells(self):
        for j in range(self._num_cols):
            column=[]
            for i in range(self._num_rows):
                column.append(Cell(self._win))                
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(j,i)
    def _draw_cell(self,i,j):
        base_shift=10
        self._cells[j][i].draw(j*self._cell_size_x+base_shift,i*self._cell_size_y+base_shift,(j+1)*self._cell_size_x+base_shift,(i+1)*self._cell_size_y+base_shift)
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
