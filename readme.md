# Welcome to Mario{Ripoff}

*Coded by:* **Rizwan Ali**

----------


About The Game
-------------

>**Super Mario Bros** is a platform video game developed and published by Nintendo. The successor to the 1983 arcade game, Mario Bros., it was released in Japan in 1985 for the Famicom, and in North America and Europe for the Nintendo Entertainment System (NES) in 1985 and 1987 respectively. Players control Mario, or his brother Luigi in the multiplayer mode, as they travel the Mushroom Kingdom to rescue Princess Toadstool from the antagonist, Bowser.

For more information click [here](https://en.wikipedia.org/wiki/Super_Mario_Bros.).

----------


Rules of the Game
-------------------

> - You control Mario throughout his efforts to reach the end of the road. In order to do this, you must destroy your enemies and boss. (Only a single level implemented in this rendition of the game.)
> - Enemies are undergoing walk in a specific pattern, but *contact* with them will reduce your life.
> - You have 3 lives for your Mario, getting killed 3 times will result in a **GAME OVER**.
> - The Mario can jump over enemies and boss and can eventually destroy them. 
> - Destroying each bricks adds 50 points to the score, while killing each enemy adds 100 points.
> - Picking a coin adds 20
>- There is a powerup which can give you the power of "Teleport Jump" , i.e., you will teleport while jumping, meaning contact with bricks won't stop you from going up.

------------------------

Description of Classes Created
--------------------------------------------
#### Board:
The board class creates a 30X90 board for gameplay, with floor, scenery and pits. It also comprises of a print_board function to take a print of the board.The complete level is stored in a different list of list.It displays the current "wiindow" of that main board.
#### Bricks:
The Brick class adds bricks to the board in empty spaces. It inherits the Board class.
#### Mario:
The Mario class has all the variables and functionality of Mario, this includes the generation, movement and bomb planting. This inherits Enemy.
#### Enemy:
The Enemy class and adds enemies to the board, it manages the motion, deletion, generation and functionality of enemies.
#### Boss:
Boss class manages the generation of boss and printing it.

__________________

How To Play:
------------------
>- Run the following code to start the game.
```
python3 run.py
```
>- Press enter to start the game.
>- 'w, a, d' use these controls for up, left, and right.
>- press 'q' to quit.

___________________
