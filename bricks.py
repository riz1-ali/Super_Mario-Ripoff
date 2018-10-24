'''
Generating bricks on board
'''
from board import Board


class Bricks(Board):
    '''
    Define the necessary parameters and functions
    '''
    @staticmethod
    def make_brick(x_coor, y_coor, l_coor, r_coor):
        '''
        Make Bricks on board
        '''
        Board.main_board[x_coor][y_coor] = Board.main_board[x_coor][y_coor + 1] = ":"
        Board.main_board[x_coor +
                         1][y_coor] = Board.main_board[x_coor +
                                                       1][y_coor +
                                                          1] = "1"
        if y_coor >= l_coor and y_coor <= r_coor:
            Board.board[x_coor][y_coor] = Board.board[x_coor][y_coor + 1] = ":"
            Board.board[x_coor +
                        1][y_coor] = Board.board[x_coor +
                                                 1][y_coor +
                                                    1] = "1"
