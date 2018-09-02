from board import Board

class Bricks(Board):
    def make_brick(self,x,y,l,r):
        Board.main_board[x][y]=Board.main_board[x][y+1]=":"
        Board.main_board[x+1][y]=Board.main_board[x+1][y+1]="1"
        if y>=l and y<=r:
            Board.board[x][y]=Board.board[x][y+1]=":"
            Board.board[x+1][y]=Board.board[x+1][y+1]="1"
        