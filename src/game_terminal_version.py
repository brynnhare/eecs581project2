#! python3
# main game loop and core logic
'''
Program: Battleship
Description: This program will be a functional two player game of battleship. This
    file contains the main game loop and core logic.
Output: A game of battleship.
Authors: Brynn Hare, Micah Borghese, Katelyn Accola, Nora Manolescu, and Kyle Johnson
Creation date: 9/4/2024
'''

import sys

player1 = 1
player2 = 2


# class Game:
    # def __init__(self):
    #     pass
    
    # def draw_boards(self):
    #     player1_board.draw()
    #     player2_board.draw()

    #     ship = player2_ships.get_1x4("B", 5, orientation="horizontal")  # my example: ship on Player 2's board
    #     # note that this returns a list of tuples representing the squares the ship occupies
    #     player2_ships.remove_ship(ship)  # remove ship from Player 2's board

    #     screen.blit(player1_board.surface, (0,0))
    #     screen.blit(player2_board.surface, ((WIDTH + 50) // 2, 0)) 

    # def update(self):
    #     screen.fill(Colors().get_white())
    #     self.draw_boards()
    #     pygame.display.update()

class Board: # Nora can do this 
    def __init__(self, player_num):
        self.player_num = player_num
        self.board = [["~" for _ in range(10)] for _ in range(10)]
        self.map = [] # keep track of coordinates?

        # Ship: O
        # Ship hit: X
        # Ship sunk: *
        # Open spot: ~

    def display_board(self):
        # Display columns denoted A-J
        print(" ".join(chr(ord('A') + i) for i in range(10)))

        # Display rows denoted 1-10
        for i, row in enumerate(self.board):
            print(" ".join(row) + f" {i + 1}")

    def is_empty(self):
        # Check if spot is free
        pass


class Ships: # I, Brynn, can do this class?
    #class that handles 1b; assigning the correct number of ships to a user
    def __init__(self, player_num):
        self.player_num = player_num #this will be put in by us each time they switch, to reprsent player 1 or 2
        self.num_ships = 0 #this is provided by the player later (must be numbers 1-5 inclusively)
        self.ship_types = [] #empty list to hold the sizes of the ships

    def choose_ships(self): #the player must select the number of ships they want to have
        num_ships = int(input("Choose the number of ships for your board (1-5): "))
        self.num_ships = num_ships
        while (1 > self.num_ships > 5): #checking for invalid ship values
             new_num = int(input("Invalid number of ships. Select a new number: ")) #prompt for another number ***THIS CAN BE CHANGED JUST AN INITIAL PHASE***
             self.num_ships = new_num #assign the new number to be the number of ships

    def load_types(self): #this forms the list with the sizes of the ships
        i = 1 #initializing for the while loop
        while i < (self.num_ships + 1): #while the current ship number is less than one extra than the number of ships chosen
            self.ship_types.append([1, i]) #append to the list. [1, 1] represents 1 x 1. [1, 2] represents 1 x 2...etc.
            i += 1 #increase the while loop

    def place(self): #place the ships on the board
        pass

    # def orientation()

    #need to have a function that allows for the players to turn the pieces (swap the x and y values of the list?)
    #need to connect to the gameboard class to "remember" where the pieces are located

class Fire:
    # need a function to account for "firing" that needs to check that it is a valid space, if yes reply with hit or miss
    #need a function to update the board
    pass

class SwitchPlayers:
    #this can be used anytime to move from player 1 to 2 
    def __init__(self, player_num):
        self.player_num = player_num
    
    def change(self):
        if self.player_num == 1:
            self.player_num = 2
        else: 
            self.player_num == 1
            
    def begin_turn(self):
        print("Begin Player", self.player_num,"'s Turn (Press Enter)") #Begins player turn waits till theres an input
        input()
        
    def end_turn(self):
        print("End Player", self.player_num,"'s Turn (Press Enter)")
        input()
    pass

class DestroyShip: 
    #needs to keep track of the ship_types list and the board, if a ship is gone it sunk
    pass

class DisplayBoard:
    #class responsible for displaying the board
    #differentiate miss with hit
    pass

class GameOver:
    #Change to function
    #display the correct player as the winner if they sunk all other ships
    pass

if __name__ == '__main__':
    #start the game
    board1 = Board(player1) #board1 represents player 1's board
    board2 = Board(player2) #board2 represents player 2's board
    ships1 = Ships(player1) #create an ships class for player 1
    ships2 = Ships(player2) #create an ships class for player 2
    switchcurrent1 = SwitchPlayers(player1) #class to switch while its player 1 turn
    switchcurrent2 = SwitchPlayers(player2) #class to switch while its player 2 turn
    switchcurrent1.begin_turn() #prompt player 1 to begin first turn
    ships1.choose_ships() #prompt player 1 with the
    ships1.load_types() #create the list of ships for player 1
    board1.display_board() #display the blank board
    for ship in ships1.ship_types:
        ships1.place()
        board1.display_board()
    switchcurrent1.end_turn()
    switchcurrent2.begin_turn()
    ships2.choose_ships() #prompt player 2 with the
    ships2.load_types() #create the list of ships for player 2
    board2.display_board() #display the blank board
    for ship in ships2.ship_types:
        ships2.place()
        board2.display_board()
    switchcurrent2.end_turn()
    





    
    
