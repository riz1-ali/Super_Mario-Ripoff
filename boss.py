'''
Module to create boss
'''
from board import Board


class Boss():
    '''
    Class to create boss
    '''
    x_head = 0
    legs = 0

    def generate_boss(self, x_coor, y_coor, l_coor, r_coor):
        '''
        Create boss on board
        '''
        self.x_head = x_coor
        self.legs = y_coor
        Board.main_board[x_coor][y_coor] = Board.main_board[x_coor][y_coor + 1] = "B"
        Board.main_board[x_coor - 1][y_coor] = Board.main_board[x_coor - 1][y_coor + 1] = "B"
        if l_coor <= y_coor and y_coor <= r_coor:
            Board.board[x_coor][y_coor - l_coor] = Board.board[x_coor][y_coor - l_coor + 1] = "B"
            Board.board[x_coor - 1][y_coor - l_coor
                                   ] = Board.board[x_coor - 1][y_coor - l_coor + 1] = "B"

    def boss_pos(self):
        '''
        Return boss' position to go
        '''
        return self.legs + 10

    def bos_p(self):
        '''
        Return boss' current position
        '''
        return self.legs

    def move_boss(self, l_coor, r_coor, sign):
        '''
        Move Boss on board (it is a smart enemy, so follows Mario)
        '''
        if sign == '+':
            Board.main_board[self.x_head][self.legs
                                         ] = Board.main_board[self.x_head][self.legs + 1] = " "
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = " "
            Board.board[self.x_head][self.legs - \
                l_coor] = Board.board[self.x_head][self.legs - l_coor + 1] = " "
            Board.board[self.x_head -
                        1][self.legs -
                           l_coor] = Board.board[self.x_head -
                                                 1][self.legs -
                                                    l_coor +
                                                    1] = " "
            self.legs += 1
            Board.main_board[self.x_head][self.legs
                                         ] = Board.main_board[self.x_head][self.legs + 1] = "B"
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = "B"
            if l_coor <= self.legs and self.legs <= r_coor:
                Board.board[self.x_head][self.legs - \
                    l_coor] = Board.board[self.x_head][self.legs - l_coor + 1] = "B"
                Board.board[self.x_head -
                            1][self.legs -
                               l_coor] = Board.board[self.x_head -
                                                     1][self.legs -
                                                        l_coor +
                                                        1] = "B"
        elif Board.main_board[self.x_head][self.legs - 1
                                          ] != ':' and Board.main_board[self.x_head - 1
                                                                       ][self.legs - 1] != ':':
            Board.main_board[self.x_head][self.legs
                                         ] = Board.main_board[self.x_head][self.legs + 1] = " "
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = " "
            Board.board[self.x_head][self.legs - \
                l_coor] = Board.board[self.x_head][self.legs - l_coor + 1] = " "
            Board.board[self.x_head -
                        1][self.legs -
                           l_coor] = Board.board[self.x_head -
                                                 1][self.legs -
                                                    l_coor +
                                                    1] = " "
            self.legs -= 1
            Board.main_board[self.x_head][self.legs
                                         ] = Board.main_board[self.x_head][self.legs + 1] = "B"
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = "B"
            if l_coor <= self.legs and self.legs <= r_coor:
                Board.board[self.x_head][self.legs - \
                    l_coor] = Board.board[self.x_head][self.legs - l_coor + 1] = "B"
                Board.board[self.x_head -
                            1][self.legs -
                               l_coor] = Board.board[self.x_head -
                                                     1][self.legs -
                                                        l_coor +
                                                        1] = "B"

    def boss_collision(self, arr):
        '''
        Check if boss collides with enemy
        '''
        if Board().board[arr[0]][arr[2]] == 'B' \
            or Board().board[arr[0]][arr[2] + 1] == 'B' \
            or Board().board[arr[1]][arr[3]] == 'B' \
            or Board().board[arr[1]][arr[3] + 1] == 'B':
            return 1
        return 0
