'''
Module for board
'''


class Board():
    '''
    Class for Board
    '''
    board = [[] for i in range(0, 30)]
    cur_left = 0
    cur_right = 89
    main_board = [[] for i in range(0, 30)]
    enemy = []
    for i in range(0, 30):
        if i > 25:
            wall = ":"
        else:
            wall = " "
        for j in range(0, 500):
            main_board[i].append(wall)
    for i in range(0, 30):
        for j in range(0, 90):
            board[i].append(main_board[i][j + cur_left])

    def cloud_make(self, x_coor, y_coor):
        '''
        Function to create clouds
        '''
        for i in range(0, 10):
            self.main_board[x_coor][y_coor + i] = self.main_board[x_coor][y_coor - i] = "_"
        for i in range(0, 2):
            self.main_board[x_coor - i][y_coor - 10 - i] = "("
            self.main_board[x_coor - i][y_coor + 10 + i] = ")"
        for i in range(0, 2):
            self.main_board[x_coor - 2 - i][y_coor - 12 + i] = "("
            self.main_board[x_coor - 2 - i][y_coor + 12 - i] = ")"
        for i in range(0, 6):
            self.main_board[x_coor - 4][y_coor - 10 +
                                        i] = self.main_board[x_coor - 4][y_coor + 10 - i] = "_"
        for i in range(0, 2):
            self.main_board[x_coor - 4 - i][y_coor - 5 - i] = "("
            self.main_board[x_coor - 4 - i][y_coor + 5 + i] = ")"
        for i in range(0, 2):
            self.main_board[x_coor - 6 - i][y_coor - 5 + i] = "("
            self.main_board[x_coor - 6 - i][y_coor + 5 - i] = ")"
        for i in range(0, 4):
            self.main_board[x_coor - 7][y_coor + i] = self.main_board[x_coor - 7][y_coor - i] = "+"
        if self.cur_left <= y_coor - 10 and self.cur_right >= y_coor + 10:
            for i in range(0, 10):
                self.board[x_coor][y_coor + i] = self.board[x_coor][y_coor - i] = "_"
            for i in range(0, 2):
                self.board[x_coor - i][y_coor - 10 - i] = "("
                self.board[x_coor - i][y_coor + 10 + i] = ")"
            for i in range(0, 2):
                self.board[x_coor - 2 - i][y_coor - 12 + i] = "("
                self.board[x_coor - 2 - i][y_coor + 12 - i] = ")"
            for i in range(0, 6):
                self.board[x_coor - 4][y_coor - 10 +
                                       i] = self.board[x_coor - 4][y_coor + 10 - i] = "_"
            for i in range(0, 2):
                self.board[x_coor - 4 - i][y_coor - 5 - i] = "("
                self.board[x_coor - 4 - i][y_coor + 5 + i] = ")"
            for i in range(0, 2):
                self.board[x_coor - 6 - i][y_coor - 5 + i] = "("
                self.board[x_coor - 6 - i][y_coor + 5 - i] = ")"
            for i in range(0, 4):
                self.board[x_coor - 7][y_coor + i] = self.board[x_coor - 7][y_coor - i] = "+"

    def pit_make(self, x_coor):
        '''
        Make pit on Board
        '''
        for j in range(26, 30):
            for i in range(0, 5):
                if j != 26:
                    self.main_board[j][x_coor - i] = self.main_board[j][x_coor + i] = " "
                else:
                    self.main_board[j][x_coor - i] = self.main_board[j][x_coor + i] = "'"
        if self.cur_left <= x_coor - 2 and self.cur_right >= x_coor + 2:
            for j in range(26, 30):
                for i in range(0, 5):
                    if j != 26:
                        self.board[j][x_coor - i] = self.board[j][x_coor + i] = " "
                    else:
                        self.board[j][x_coor - i] = self.board[j][x_coor + i] = "'"

    def pillar_make(self, x_coor):
        '''
        Make pillars on board
        '''
        for j in range(22, 26):
            for i in range(0, 3):
                self.main_board[j][x_coor - i] = self.main_board[j][x_coor + i] = ":"
        if self.cur_left <= x_coor - 2 and self.cur_right >= x_coor + 2:
            for j in range(22, 26):
                for i in range(0, 3):
                    self.board[j][x_coor - i] = self.board[j][x_coor + i] = ":"

    def remove_brick(self, x_coor, y_coor):
        '''
        Delete bricks from board
        '''
        self.board[x_coor][y_coor] = self.board[x_coor][y_coor + 1] = " "
        self.board[x_coor - 1][y_coor] = self.board[x_coor - 1][y_coor + 1] = " "
        self.main_board[x_coor][y_coor +
                                self.cur_left] = self.main_board[x_coor][y_coor +
                                                                         1 +
                                                                         self.cur_left] = " "
        self.main_board[x_coor -
                        1][y_coor +
                           self.cur_left] = self.main_board[x_coor -
                                                            1][y_coor +
                                                               1 +
                                                               self.cur_left] = " "

    def coin_make(self, x_coor, y_coor):
        '''
        Make coins on board
        '''
        self.main_board[x_coor][y_coor + self.cur_left] = "C"
        if self.cur_left <= y_coor and self.cur_right >= y_coor:
            self.board[x_coor][y_coor] = "C"

    def remove_coin(self, x_coor, y_coor):
        '''
        Remove Coins from board
        '''
        self.board[x_coor][y_coor] = " "
        self.main_board[x_coor][y_coor + self.cur_left] = " "

    def left(self):
        '''
        Return left index of main board
        '''
        return self.cur_left

    def right(self):
        '''
        Return right index of main board
        '''
        return self.cur_right

    def powerup(self, x_coor, y_coor):
        '''
        Print Powerup to jump on board
        '''
        self.main_board[x_coor][y_coor + self.cur_left] = "J"
        if self.cur_left <= y_coor and self.cur_right >= y_coor:
            self.board[x_coor][y_coor] = "J"

    def mountain_make(self, x_coor, y_coor):
        '''
        Make mountains on board
        '''
        for i in range(0, 10):
            if i != 0:
                self.main_board[x_coor + i][y_coor - i] = "/"
                self.main_board[x_coor + i][y_coor + i] = "\\"
            else:
                self.main_board[x_coor + i][y_coor - i] = "^"
        if self.cur_left <= y_coor - 10 and self.cur_right >= y_coor + 10:
            for i in range(0, 10):
                if i != 0:
                    self.board[x_coor + i][y_coor - i] = "/"
                    self.board[x_coor + i][y_coor + i] = "\\"
                else:
                    self.board[x_coor + i][y_coor - i] = "^"

    def print_board(self):
        '''
        Print Board
        '''
        temp = ['' for i in range(0, 30)]
        for j in range(0, 30):
            for i in range(0, 90):
                temp[j] += self.board[j][i]
        for i in range(0, 30):
            print(temp[i])

    def fix(self, xc_coor, yc_coor, h_coor, l_coor):
        '''
        Print Mario on Board
        '''
        temp = ['' for i in range(0, 30)]
        self.cur_right += 1
        self.cur_left += 1
        for i in range(0, 30):
            for j in range(0, 90):
                if j == h_coor and i == xc_coor or j == h_coor + 1 and i == xc_coor:
                    temp[i] += "H"
                elif j == l_coor and i == yc_coor or j == l_coor + 1 and i == yc_coor:
                    temp[i] += "L"
                else:
                    temp[i] += self.main_board[i][self.cur_left + j]
        for i in range(0, 30):
            for j in range(0, 90):
                self.board[i][j] = temp[i][j]
        for i in range(0, 30):
            print(temp[i])
