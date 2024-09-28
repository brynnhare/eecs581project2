# EECS 581 Project 1
Battleship!

## Description
In our game of battleship, player one and player two play on the same device. 

First, `cd` into the `src` folder. The game begins by typing `python3 game_terminal_version.py` into the terminal. 

From there, player one is prompted to begin their turn. After hitting enter, they get to pick the number of ships they want to have (1-5). The blank game board is displayed, and the player gets to place their ship (horizontally or vertically) onto the board. The board is redisplayed with each ship placement until all of their ships are placed. Then player one is prompted to end their turn. Player two will go through this same process. Players are prompted to both begin and end their turn to insure that there is no chance that they players will accidentally see the opponent’s board. From there player one gets to begin play by selecting a place to fire at. If they hit an empty space, the turn is over. If they hit a ship, they get to fire again. If a ship sinks, they are told that a ship has sunk and they get to fire again. This process continues until all ships are sunk or the opposing player wins. 