from board import Board

class Enemy:
    
    enemy = []

    def generate_enemy(self,x,y,l,r):
        Board.main_board[x][y+l]=Board.main_board[x][y+l+1]="E"
        Board.main_board[x-1][y+l]=Board.main_board[x-1][y+l+1]="E"
        self.enemy.append(y)
        if l<=y and y<=r:
            Board.board[x][y]=Board.board[x][y+1]="E"
            Board.board[x-1][y]=Board.board[x-1][y+1]="E"

    def delete_enemy(self,x,y,l):
        Board.board[x][y]=Board.board[x][y+1]=" "
        Board.board[x-1][y]=Board.board[x-1][y+1]=" "
        Board.main_board[x][y+l]=Board.main_board[x][y+l+1]=" "
        Board.main_board[x-1][y+l]=Board.main_board[x-1][y+l+1]=" "
        self.enemy.remove(y)

    def coor_fix(self):
        for i in range(0,len(self.enemy)):
            self.enemy[i]-=1
        
    def check(self,l):
        for i in self.enemy:
            if i<=l:
                self.enemy.remove(i)
    def print_enemy(self,x,l,r):
        for i in range(0,len(self.enemy)):
            try:
                if self.enemy[i]>l+1:
                    Board.main_board[x][self.enemy[i]+l]=Board.main_board[x][self.enemy[i]+l+1]=" "
                    Board.main_board[x-1][self.enemy[i]+l]=Board.main_board[x-1][self.enemy[i]+l+1]=" "
            except IndexError:
                self.enemy.remove(self.enemy[i])
            if l<=self.enemy[i] and self.enemy[i]+8<=r:
                try:
                    Board.board[x][self.enemy[i]]=Board.board[x][self.enemy[i]+1]="E"
                    Board.board[x-1][self.enemy[i]]=Board.board[x-1][self.enemy[i]+1]="E"
                except IndexError:
                    pass

    def move_enemy(self,x,l,r,sign):
        for i in range(0,len(self.enemy)):
            try:
                Board.main_board[x][self.enemy[i]+l]=Board.main_board[x][self.enemy[i]+l+1]=" "
                Board.main_board[x-1][self.enemy[i]+l]=Board.main_board[x-1][self.enemy[i]+l+1]=" "
                if l<=self.enemy[i] and self.enemy[i]<=r:
                    Board.board[x][self.enemy[i]]=Board.board[x][self.enemy[i]+1]=" "
                    Board.board[x-1][self.enemy[i]]=Board.board[x-1][self.enemy[i]+1]=" "
            
                if sign == '+' and self.enemy[i]+1<=r-1:
                     self.enemy[i]+=1
                elif sign == '-':
                    if self.enemy[i]-1>=l+1:
                        self.enemy[i]-=1
                    else:
                        self.delete_enemy(x,self.enemy[i],l)
            except IndexError:
                pass
                
    def collision(self,xh,yl,h,l,left,right):
        for i in range(0,len(self.enemy)):
            if left<= self.enemy[i] and right>=self.enemy[i]:
                if Board().board[xh][h]=='E' or Board().board[xh][h+1]=='E' or Board().board[yl][l]=='E' or Board().board[yl][l+1]=='E':
                    return 1
            break
        return 0