from window import Window
from window_objects import Point,Line,Cell
from maze import Maze

def main():
    print("Game is Beginning")
    game_window=Window(1200,800)
    maze=Maze(50,50,11,11,50,50,game_window,0)
    maze.solve_r(0,0)


    game_window.wait_for_close()




if __name__=="__main__":
    main()