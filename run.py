import os
from subprocess import call
from mario import Mario
from board import Board
from bricks import Bricks
import time

print("")
print("Welcome to Mario{Ripoff}")
print("Press enter to play")
x = input()
os.system('aplay song.wav &')
B = Board()
M = Mario()
M.generate_mario()
M.generate_boss(25,420,B.left(),B.right())

for i in range(20,400,100):
    B.cloud_make(10,i)
    B.cloud_make(10,i+50)
    B.mountain_make(16,i+30)
    B.pit_make(i)
    B.pillar_make(i+60)
    for j in range(0,10):
        if j%2:
            B.coin_make(25,i+j+40)
    Bricks().make_brick(18,i+20,B.left(),B.right())
    M.generate_enemy(25,i+10,B.left(),B.right())
ft = time.time()
c=0
bft = time.time()
B.powerup(25,40)
while True:
    os.system("tput reset")
    M.print_scolife()
    B.print_board()
    if time.time()>ft+1 and time.time()-ft<2 and M.stat():
        c+=1
        if c%13<=6:
            M.move_enemy(25,B.left(),B.right(),'+')
        else:
            M.move_enemy(25,B.left(),B.right(),'-')
        ft=time.time()
    if time.time()>bft+0.25 and time.time()-bft<0.5 and M.stat():
        if M.pos() > M.bos_p()-M.board_left():
            M.call_boss('+')
        else:
            M.call_boss('-')
        bft=time.time()
    M.check(B.left())
    M.print_enemy(25,B.left(),B.right())
    M.move_mario()
