from window import Window
from window_objects import Point,Line,Cell

def main():
    print("Game is Beginning")
    game_window=Window(1200,800)
    cell1=Cell(50,100,150,200,game_window)
    cell1.draw()
    cell2=Cell(150,100,250,200,game_window)
    cell2.draw()
    cell3=Cell(250,100,350,200,game_window)
    cell3.draw()

    cell1.draw_move(cell2,True)
    cell2.draw_move(cell3,False)
    game_window.wait_for_close()




if __name__=="__main__":
    main()