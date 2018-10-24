'''
Module to create enemies
'''
from board import Board


class Enemy:
    '''
    Class for enemies
    '''
    enemy = []

    def generate_enemy(self, arr):
        '''
        Spawn enemies on board
        '''
        Board.main_board[arr[0]][arr[1] + arr[2]
                                ] = Board.main_board[arr[0]][arr[1] + arr[2] + 1] = "E"
        Board.main_board[arr[0] - 1][arr[1] +
                                     arr[2]] = Board.main_board[arr[0] - 1
                                                               ][arr[1] + arr[2] + 1] = "E"
        self.enemy.append(arr[1])
        if arr[2] <= arr[1] and arr[1] <= arr[3]:
            Board.board[arr[0]][arr[1]] = Board.board[arr[0]][arr[1] + 1] = "E"
            Board.board[arr[0] - 1][arr[1]
                                   ] = Board.board[arr[0] - 1][arr[1] + 1] = "E"

    def delete_enemy(self, x_coor, y_coor, l_coor):
        '''
        Delete enemies from the board
        '''
        Board.board[x_coor][y_coor] = Board.board[x_coor][y_coor + 1] = " "
        Board.board[x_coor - 1][y_coor] = Board.board[x_coor - 1][y_coor + 1] = " "
        Board.main_board[x_coor][y_coor + l_coor] = Board.main_board[x_coor][y_coor +
                                                                             l_coor + 1] = " "
        Board.main_board[x_coor - 1][y_coor +
                                     l_coor] = Board.main_board[x_coor - 1][y_coor +
                                                                            l_coor + 1] = " "
        self.enemy.remove(y_coor)

    def coor_fix(self):
        '''
        Move enemies
        '''
        for i in range(0, len(self.enemy)):
            self.enemy[i] -= 1

    def check(self, l_coor):
        '''
        Remove enemy if it went out of board
        '''
        for i in self.enemy:
            if i <= l_coor:
                self.enemy.remove(i)

    def print_enemy(self, x_coor, l_coor, r_coor):
        '''
        Print enemies on board
        '''
        for i in range(0, len(self.enemy)):
            try:
                if self.enemy[i] > l_coor + 1:
                    Board.main_board[x_coor][self.enemy[i] +
                                             l_coor] = Board.main_board[x_coor][self.enemy[i] +
                                                                                l_coor +
                                                                                1] = " "
                    Board.main_board[x_coor -
                                     1][self.enemy[i] +
                                        l_coor] = Board.main_board[x_coor -
                                                                   1][self.enemy[i] +
                                                                      l_coor +
                                                                      1] = " "
            except IndexError:
                self.enemy.remove(self.enemy[i])
            if l_coor <= self.enemy[i] and self.enemy[i] + 8 <= r_coor:
                try:
                    Board.board[x_coor][self.enemy[i]
                                       ] = Board.board[x_coor][self.enemy[i] + 1] = "E"
                    Board.board[x_coor - 1][self.enemy[i]
                                           ] = Board.board[x_coor - 1][self.enemy[i] + 1] = "E"
                except IndexError:
                    pass

    def move_enemy(self, x_coor, l_coor, r_coor, sign):
        '''
        Move enemies on board
        '''
        for i in range(0, len(self.enemy)):
            try:
                Board.main_board[x_coor][self.enemy[i] +
                                         l_coor] = Board.main_board[x_coor][self.enemy[i] +
                                                                            l_coor +
                                                                            1] = " "
                Board.main_board[x_coor -
                                 1][self.enemy[i] +
                                    l_coor] = Board.main_board[x_coor -
                                                               1][self.enemy[i] +
                                                                  l_coor +
                                                                  1] = " "
                if l_coor <= self.enemy[i] and self.enemy[i] <= r_coor:
                    Board.board[x_coor][self.enemy[i]
                                       ] = Board.board[x_coor][self.enemy[i] + 1] = " "
                    Board.board[x_coor - 1][self.enemy[i]
                                           ] = Board.board[x_coor - 1][self.enemy[i] + 1] = " "

                if sign == '+' and self.enemy[i] + 1 <= r_coor - 1:
                    self.enemy[i] += 1
                elif sign == '-':
                    if self.enemy[i] - 1 >= l_coor + 1:
                        self.enemy[i] -= 1
                    else:
                        self.delete_enemy(x_coor, self.enemy[i], l_coor)
            except IndexError:
                pass

    def collision(self, arr):
        '''
        Check if an enemy collides with mario
        '''
        for i in range(0, len(self.enemy)):
            if arr[4] <= self.enemy[i] and arr[5] >= self.enemy[i]:
                if Board().board[arr[0]][arr[2]] == 'E' or Board(
                ).board[arr[0]][arr[2] + 1] == 'E' or Board(
                ).board[arr[1]][arr[3]] == 'E' or Board().board[arr[1]][arr[3] + 1] == 'E':
                    return 1
            break
        return 0
