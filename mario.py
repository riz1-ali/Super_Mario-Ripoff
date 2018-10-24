'''
Module for Mario
'''
import signal
import os
import time
from board import Board
from getch import _getchlinux as getChar
from alarmexception import AlarmException
from enemy import Enemy
from boss import Boss

b = Board()


class Mario(Enemy, Boss):
    '''
    Class for Mario
    '''
    head = 0
    legs = 0
    x_head = 24
    y_legs = 25
    jumping = 0
    ft = 0
    f = 0
    jump_up = 1
    frame = 0
    jump_mark = 0
    fall = 0
    fall_down = 0
    block = 0
    score = 0
    coins = 0
    lives = 3
    boss_lives = 3
    keypress = 1
    frame_move = 1
    life_clock = time.time()
    jump_timer = 0

    def generate_mario(self):
        '''
        Create Mario on Board
        '''
        b.board[self.x_head][self.head] = b.board[self.x_head][self.head + 1] = "H"
        b.board[self.y_legs][self.legs] = b.board[self.y_legs][self.legs + 1] = "L"

    def pos(self):
        '''
        Function for Mario's Position
        '''
        return self.head

    def print_scolife(self):
        '''
        Function to print scoreboard
        '''
        print("")
        print("SCORE:" + str(self.score))
        print("LIVES:" + str(self.lives))
        print("COINS:" + str(self.coins))
        print("")

    def call_boss(self, sign):
        '''
        Create Boss if he's in view
        '''
        if b.left() <= self.boss_pos() and self.boss_pos() <= b.right():
            self.move_boss(b.left(), b.right(), sign)

    def stat(self):
        '''
        Return how much blocks the frame has moved
        '''
        return self.frame_move

    def board_left(self):
        '''
        Return left index of board
        '''
        return b.left()

    def move_mario(self):
        '''
        Move Mario on Board
        '''
        def alarmhandler(signum, frame):
            '''
            Function for Error Handling
            '''
            raise AlarmException

        def user_input(timeout=0.05):
            '''
            Take user input from terminal
            '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)

                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        key = user_input()

        if Mario.lives == 0:
            os.system("tput reset")
            os.system('killall -9 aplay')
            print("Game Over")
            quit()

        if Mario.jump_timer + 10 < time.time():
            Mario.jump_up = 1
        
        en_arr = [Mario.x_head,
                  Mario.y_legs,
                  Mario.head,
                  Mario.legs,
                  b.left(),
                  b.right()]

        if Enemy().collision(
                en_arr) and Mario.life_clock + 1 < time.time():
            Mario.life_clock = time.time()
            Mario.lives -= 1

        if Boss().boss_collision(
           [Mario.x_head,
            Mario.y_legs,
            Mario.head,
            Mario.legs,
            b.left(),
            b.right()]) and Mario.life_clock + 1 < time.time():
            Mario.life_clock = time.time()
            Mario.lives -= 1

        if key == 'q':
            Mario.frame = 0
            os.system("tput reset")
            os.system('killall -9 aplay')
            print("Due play it afterwards")
            quit()

        if key == 'l':
            Mario.lives += 1

        if key == 'd' and Mario.head <= 88 and b.cur_left + Mario.head <= 448 and b.board[Mario.x_head][Mario.head + 1] != ":" and b.board[Mario.y_legs][
                Mario.legs + 1] != ":" and b.board[Mario.x_head][Mario.head + 2] != ":" and b.board[Mario.y_legs][Mario.legs + 2] != ":" and Mario.keypress == 1:
            Mario.frame += 1
            b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
            b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
            if Mario.head <= 30 or b.cur_right >= 450 or Mario.frame <= 1:
                if b.board[Mario.y_legs][Mario.legs + 1] == "C":
                    Mario.coins += 1
                    Mario.score += 20
                    b.main_board[Mario.y_legs][Mario.legs +
                                               1 + b.cur_left] = " "
                    b.board[Mario.y_legs][Mario.legs + 1] = " "
                elif b.board[Mario.y_legs][Mario.legs + 1] == "J":
                    Mario.jump_timer = time.time()
                    Mario.jump_up = 2
                    b.main_board[Mario.y_legs][Mario.legs +
                                               1 + b.cur_left] = " "
                    b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.head += 1
                Mario.legs += 1
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                b.print_board()
            else:
                Mario.frame_move = 0
                os.system("tput reset")
                if b.board[Mario.y_legs][Mario.legs + 2] == "C":
                    Mario.coins += 1
                    Mario.score += 20
                    b.main_board[Mario.y_legs][Mario.legs +
                                               2 + b.cur_left] = " "
                    b.board[Mario.y_legs][Mario.legs + 2] = " "
                elif b.board[Mario.y_legs][Mario.legs + 2] == "J":
                    Mario.jump_timer = time.time()
                    Mario.jump_up = 2
                    b.main_board[Mario.y_legs][Mario.legs +
                                               2 + b.cur_left] = " "
                    b.board[Mario.y_legs][Mario.legs + 2] = " "
                b.fix(Mario.x_head, Mario.y_legs, Mario.head, Mario.legs)
                Enemy().coor_fix()
                Mario.frame_move = 1

        if key == 'a' and Mario.head >= 1 and b.board[Mario.x_head][Mario.head -
                                                                    1] != ":" and b.board[Mario.y_legs][Mario.legs -
                                                                                                        1] != ":" and b.board[Mario.x_head][Mario.head -
                                                                                                                                            2] != ":" and b.board[Mario.y_legs][Mario.legs -
                                                                                                                                                                                2] != ":" and Mario.keypress == 1:
            Mario.frame = 0
            b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
            b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
            if b.board[Mario.y_legs][Mario.legs - 1] == "C":
                Mario.coins += 1
                Mario.score += 20
                b.main_board[Mario.y_legs][Mario.legs - 1 + b.cur_left] = " "
                b.board[Mario.y_legs][Mario.legs - 1] = " "
            elif b.board[Mario.y_legs][Mario.legs - 1] == "J":
                Mario.jump_timer = time.time()
                Mario.jump_up = 2
                b.main_board[Mario.y_legs][Mario.legs - 1 + b.cur_left] = " "
                b.board[Mario.y_legs][Mario.legs - 1] = " "

            Mario.head -= 1
            Mario.legs -= 1
            b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
            b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
            b.print_board()

        if key == 'w' and Mario.jumping == 0 and Mario.block == 0 and Mario.keypress == 1 and b.board[
                Mario.x_head - 1][Mario.head] != ':' and b.board[Mario.x_head - 1][Mario.head + 1] != ':':
            Mario.frame = 0
            Mario.jumping = 1
            Mario.jump_mark = 0
            Mario.fall = 0
            Mario.fall_down = 0
            Mario.ft = time.time()
            Mario.f = 0

        if b.board[Mario.x_head -
                   1][Mario.head] == "1" and b.board[Mario.x_head -
                                                     1][Mario.head +
                                                        1] == "1":
            Mario.jumping = 0
            Mario.fall = 1
            b.board[Mario.x_head -
                    1][Mario.head] = b.board[Mario.x_head -
                                             1][Mario.head +
                                                1] = "0"

        if b.board[Mario.x_head -
                   1][Mario.head] == "0" and b.board[Mario.x_head -
                                                     1][Mario.head +
                                                        1] == "0" and Mario.fall == 0:
            b.remove_brick(Mario.x_head - 1, Mario.head)
            Mario.score += 50

        if Mario.jump_mark == 9 and b.board[Mario.y_legs +
                                            1][Mario.legs] == "E" and b.board[Mario.y_legs +
                                                                              1][Mario.legs +
                                                                                 1] == "E":
            Mario.score += 100
            Mario.en_flag = 0
            Mario.keypress = 0
            Enemy().delete_enemy(Mario.y_legs + 1, Mario.legs, b.left())
            Mario.keypress = 1

        if Mario.jump_mark == 9 and b.board[Mario.y_legs +
                                            1][Mario.legs] == "B" and b.board[Mario.y_legs +
                                                                              1][Mario.legs +
                                                                                 1] == "B":
            Mario.score += 500
            Mario.boss_lives -= 1
            if Mario.boss_lives == 0:
                print("You Won")
                os.system('killall -9 aplay')
                quit()

        if Mario.jumping == 1:
            if time.time() < Mario.ft + 0.1 and Mario.f == 0:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head -= Mario.jump_up
                Mario.y_legs -= Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 1
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 1:
                Mario.jumping = 0
            if time.time() < Mario.ft + 0.2 and time.time() > Mario.ft + 0.1 and Mario.f == 1:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head -= Mario.jump_up
                Mario.y_legs -= Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 0
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 2:
                Mario.jumping = 0
            if time.time() < Mario.ft + 0.3 and time.time() > Mario.ft + 0.2 and Mario.f == 0:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head -= Mario.jump_up
                Mario.y_legs -= Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 1
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 3:
                Mario.jumping = 0
            if time.time() < Mario.ft + 0.4 and time.time() > Mario.ft + 0.3 and Mario.f == 1:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head -= Mario.jump_up
                Mario.y_legs -= Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 0
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 4:
                Mario.jumping = 0
            if time.time() < Mario.ft + 0.6 and time.time() > Mario.ft + 0.4 and Mario.f == 0:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head -= Mario.jump_up
                Mario.y_legs -= Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 1
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 5:
                Mario.jumping = 0
            if time.time() < Mario.ft + 0.8 and time.time() > Mario.ft + 0.6 and Mario.f == 1:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head += Mario.jump_up
                Mario.y_legs += Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 0
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 6:
                Mario.jumping = 0
            if time.time() < Mario.ft + 0.9 and time.time() > Mario.ft + 0.8 and Mario.f == 0:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head += Mario.jump_up
                Mario.y_legs += Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 1
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 7:
                Mario.jumping = 0
            if time.time() < Mario.ft + 1 and time.time() > Mario.ft + 0.9 and Mario.f == 1:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head += Mario.jump_up
                Mario.y_legs += Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 0
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 8:
                Mario.jumping = 0
            if time.time() < Mario.ft + 1.1 and time.time() > Mario.ft + 1 and Mario.f == 0:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head += Mario.jump_up
                Mario.y_legs += Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 1
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 9:
                Mario.jumping = 0
            if time.time() < Mario.ft + 1.2 and time.time() > Mario.ft + 1.1 and Mario.f == 1:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head += Mario.jump_up
                Mario.y_legs += Mario.jump_up
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.f = 0
                Mario.jump_mark += 1
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":" and Mario.jump_mark == 10:
                Mario.jumping = 0
            elif Mario.jump_mark == 10:
                Mario.jumping = 0
                Mario.fall = 1

        if Mario.y_legs == 29:
            os.system("tput reset")
            print("Game Over")
            os.system('killall -9 aplay')
            quit()

        if (b.board[Mario.y_legs +
                    1][Mario.legs] == " " or b.board[Mario.y_legs +
                                                     1][Mario.legs] == "'") and (b.board[Mario.y_legs +
                                                                                         1][Mario.legs +
                                                                                            1] == " " or b.board[Mario.y_legs +
                                                                                                                 1][Mario.legs +
                                                                                                                    1] == "'") and Mario.jumping == 0:
            Mario.fall = 1
            Mario.act = 1
            Mario.jumping = 0
            Mario.block = 1

        if Mario.fall:
            Mario.fall_down = 1
            Mario.ft = time.time()

        if Mario.fall_down:
            Mario.fall = 0
            if b.board[Mario.y_legs +
                       1][Mario.legs] == ":" or b.board[Mario.y_legs +
                                                        1][Mario.legs +
                                                           1] == ":":
                Mario.fall_down = 0
                Mario.jumping = 0
                Mario.block = 0
            if time.time() < Mario.ft + 0.3 and time.time() > Mario.ft:
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = " "
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = " "
                Mario.x_head += 1
                Mario.y_legs += 1
                b.board[Mario.x_head][Mario.head] = b.board[Mario.x_head][Mario.head + 1] = "H"
                b.board[Mario.y_legs][Mario.legs] = b.board[Mario.y_legs][Mario.legs + 1] = "L"
                Mario.ft -= 0.5
