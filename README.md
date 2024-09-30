# EECS 581 Project 2
Battleship!

## Description
In our game of battleship, player one and player two play on the same device. 

First, `cd` into the `src` folder. The game begins by typing `python3 game_terminal_version.py` into the terminal. 

The player is asked if they would like to play in a 1 or 2 player game. A 1 player game will have the player compete against AI. There are 3 game modes: easy, medium, and hard. In the easy mode the computer fires randomly on the player's board. In the medium mode, the computer randomly fires on the player's board until they hit a ship. Once a ship is hit, the computer strategically fires for each of the following turns until the ship is sunk. In the hard mode, the computer knows where the player's ships are and will sink them all in one turn. 

If a 2 player game is selected, player one is prompted to begin their turn. After hitting enter, they get to pick the number of ships they want to have (1-5). The blank game board is displayed, and the player gets to place their ship (horizontally or vertically) onto the board. The board is redisplayed with each ship placement until all of their ships are placed. Then player one is prompted to end their turn. Player two will go through this same process. Players are prompted to both begin and end their turn to insure that there is no chance that they players will accidentally see the opponent’s board. From there player one gets to begin play by selecting a place to fire at. If they hit an empty space, the turn is over. If they hit a ship, they get to fire again. If a ship sinks, they are told that a ship has sunk and they get to fire again. This process continues until all ships are sunk or the opposing player wins. 

While the game is played, there is a scoreboard that is displayed after each turn. This board shows each player's misses, hits, and ships sunk. 
