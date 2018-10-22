from board import Board


class Boss():
    x_head = 0
    legs = 0

    def generate_boss(self, x, y, l, r):
        self.x_head = x
        self.legs = y
        Board.main_board[x][y] = Board.main_board[x][y + 1] = "B"
        Board.main_board[x - 1][y] = Board.main_board[x - 1][y + 1] = "B"
        if l <= y and y <= r:
            Board.board[x][y - l] = Board.board[x][y - l + 1] = "B"
            Board.board[x - 1][y - l] = Board.board[x - 1][y - l + 1] = "B"

    def boss_pos(self):
        return self.legs + 10

    def bos_p(self):
        return self.legs

    def move_boss(self, l, r, sign):
        if sign == '+':
            Board.main_board[self.x_head][self.legs] = Board.main_board[self.x_head][self.legs + 1] = " "
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = " "
            Board.board[self.x_head][self.legs - \
                l] = Board.board[self.x_head][self.legs - l + 1] = " "
            Board.board[self.x_head -
                        1][self.legs -
                           l] = Board.board[self.x_head -
                                            1][self.legs -
                                               l +
                                               1] = " "
            self.legs += 1
            Board.main_board[self.x_head][self.legs] = Board.main_board[self.x_head][self.legs + 1] = "B"
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = "B"
            if l <= self.legs and self.legs <= r:
                Board.board[self.x_head][self.legs - \
                    l] = Board.board[self.x_head][self.legs - l + 1] = "B"
                Board.board[self.x_head -
                            1][self.legs -
                               l] = Board.board[self.x_head -
                                                1][self.legs -
                                                   l +
                                                   1] = "B"
        elif Board.main_board[self.x_head][self.legs - 1] != ':' and Board.main_board[self.x_head - 1][self.legs - 1] != ':':
            Board.main_board[self.x_head][self.legs] = Board.main_board[self.x_head][self.legs + 1] = " "
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = " "
            Board.board[self.x_head][self.legs - \
                l] = Board.board[self.x_head][self.legs - l + 1] = " "
            Board.board[self.x_head -
                        1][self.legs -
                           l] = Board.board[self.x_head -
                                            1][self.legs -
                                               l +
                                               1] = " "
            self.legs -= 1
            Board.main_board[self.x_head][self.legs] = Board.main_board[self.x_head][self.legs + 1] = "B"
            Board.main_board[self.x_head -
                             1][self.legs] = Board.main_board[self.x_head -
                                                              1][self.legs +
                                                                 1] = "B"
            if l <= self.legs and self.legs <= r:
                Board.board[self.x_head][self.legs - \
                    l] = Board.board[self.x_head][self.legs - l + 1] = "B"
                Board.board[self.x_head -
                            1][self.legs -
                               l] = Board.board[self.x_head -
                                                1][self.legs -
                                                   l +
                                                   1] = "B"

    def boss_collision(self, xh, yl, h, l, left, right):
        if Board().board[xh][h] == 'B' or Board().board[xh][h +
                                                            1] == 'B' or Board().board[yl][l] == 'B' or Board().board[yl][l +
                                                                                                                          1] == 'B':
            return 1
        return 0
