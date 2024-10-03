# EECS 581 Project 2
Battleship!

## Description
First, `cd` into the `src` folder. The game begins by typing `python3 game_terminal_version.py` into the terminal. 

The game begines with the player being asked if they would like to play in a 1 or 2 player game. A 1 player game will have the player competeing against an AI opponent. There are 3 game difficulty modes: easy, medium, and hard. In the easy mode, the computer fires randomly on the player's board. In the medium mode, the computer randomly fires on the player's board until they hit a ship. Once a ship is hit, the computer then strategically fires for each of the following turns until the ship is sunk. In the hard mode, the computer knows where the player's ships are and will sink them all in one turn. 

If a 2 player game is selected, player one is prompted to begin their turn. After hitting enter, they get to pick the number of ships they want to have (1-5). The blank game board is displayed, and the player gets to place their ship (horizontally or vertically) onto the board. The board is redisplayed with each ship placement until all of their ships are placed, so that players can strategize their ship formation. Then player one is prompted to end their turn. Player two will go through this same process. Players are prompted to both begin and end their turn, automatically clearing the screen with the end turn, to insure that there is no chance that the players will accidentally see the opponent’s board. From there player one gets to begin game play by selecting coordinates to fire at. If they hit an empty space, the turn is over. If they hit a ship, they get to fire again. If a ship sinks, they are told that a ship has sunk and they get to fire again. With each play, the board is updated to communicate to both players where guesses have been made, and it switches to the next players turn. This process continues until all ships are sunk or a player wins the game by sinking all of their opponents ship. 

While the game is played, there is a scoreboard that is displayed after each turn. This board shows each player's misses, hits, and ships sunk. 
