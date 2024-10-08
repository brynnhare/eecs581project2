#! python3
# main game loop and core logic
'''
Program: Battleship
Description: This program will be a functional two player game of battleship. This
    file contains the main game loop and core logic. This version of the game ultimately is not used in the final product.
Output: A game of battleship.
Authors: Brynn Hare, Micah Borghese, Katelyn Accola, Nora Manolescu, and Kyle Johnson
Creation date: 9/4/2024
'''
import pygame
import sys
from gui import Board, Colors, Ships

WIDTH, HEIGHT = 1150, 600 # set GUI dimensions

player1_board = Board(WIDTH - 350, HEIGHT, board_name="Player 1") # create the board for Player 1
player2_board = Board(WIDTH - 350, HEIGHT, board_name="Player 2") # create the board for Player 2
player1_ships = Ships(player1_board.surface, player1_board.square_size) # represents the available ships for Player 1
player2_ships = Ships(player2_board.surface, player2_board.square_size) # represents the available ships for Player 2

class Game:
    """
    The main game loop and core logic for the game.
    """
    def __init__(self):
        self.ship_sizes = ['1x1', '1x2', '1x3', '1x4']
        self.player_boards = [player1_board, player2_board]
        self.player_ships = [player1_ships, player2_ships]
        self.player_focus = 0
        self.draw_boards()

        for ship_size in self.ship_sizes:
            text = f'Player {str(self.player_focus + 1)}: Click where you want your {ship_size}-long ship to be:'
            #text = 'Click again to rotate a ship, or elsewhere if ready.'
            self.player_boards[self.player_focus].show_text(text)

            x, y = self.get_input()
            if x is not None and y is not None:
                #ship = Ship(x, y, direction, self.ship_to_place)
                ship = [("A", 3)]
                if self.player_ships[self.player_focus].is_valid(ship):
                    ship_location = f"get_{ship_size}"
                    print("SHIP LOCATION:", ship_location)
                    ship_location(ship)
                else:
                    break

        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    def draw_boards(self):
        """
        Draws the boards for both players, and removes a ship from Player 2's board for testing purposes. Unfinished here.
        """
        player1_board.draw()
        player2_board.draw()

        ship = player2_ships.get_1x4("B", 5, orientation="horizontal")  # my example: ship on Player 2's board
        # note that this returns a list of tuples representing the squares the ship occupies
        player2_ships.remove_ship(ship)  # remove ship from Player 2's board

        screen.blit(player1_board.surface, (0,0))
        screen.blit(player2_board.surface, ((WIDTH + 50) // 2, 0)) 
    
    def get_input(self):
        """
        Converts mouse click events into board corrdinates, for any input
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.close()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                return x, y
        return None, None

    def update(self):
        if self.player_focus == 0:
            self.player_boards[0].show_board()
        else:
            self.player_boards[1].cover_board()
        if self.player_focus == 1:
            self.player_boards[1].show_board()
        else:
            self.player_boards[0].cover_board()
        
        pygame.display.update()

    @classmethod
    def close(cls):
        pygame.display.quit()
        pygame.quit()

class AssignShips: # I, Brynn, can do this class?
    #class that handles 1b; assigning the correct number of ships to a user
    def __init__(self, player_num, num_ships):
        self.player_num = player_num #this will be put in by us each time they switch, to reprsent player 1 or 2
        self.num_ships = num_ships #this is provided by the player (must be numbers 1-5 inclusively)

    def choose_ships(self): #the player must select the number of ships they want to have
        while (1 > self.num_ships > 5): #checking for invalid ship values
             new_num = input("Invalid number of ships. Select a new number: ") #prompt for another number ***THIS CAN BE CHANGED JUST AN INITIAL PHASE***
             self.num_ships = new_num #assign the new number to be the number of ships

class ShipTypes: #brynn can also do this class?
    #class that is determined by the combination of the num_ships and player_num of the AssignShip class
    def __init__(self, num_ships):
        self.ship_types = [] #empty list to hold the sizes of the ships
        self.num_ships = num_ships #the number of ships that the player chose 

    def load_types(self): #this forms the list with the sizes of the ships
        i = 1 #initializing for the while loop
        while i < (self.num_ships + 1): #while the current ship number is less than one extra than the number of ships chosen
            self.ship_types.append([1, i]) #append to the list. [1, 1] represents 1 x 1. [1, 2] represents 1 x 2...etc.
            i += 1 #increase the while loop

class ShipPlacement: 
    #class to control where the ships are placed on the board
    def __init__(self, player_num, ship_types):
        self.player_num = player_num
        self.ship_types = ship_types

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

class DestroyShip: 
    #needs to keep track of the ship_types list and the board, if a ship is gone it sunk
    pass

class DisplayBoard:
    #class responsible for displaying the board
    #differentiate miss with hit
    pass

class GameOver:
    #display the correct player as the winner if they sunk all other ships
    pass

if __name__ == '__main__':
    pygame.init()
    running = True # this is the 'game loop' that will be True until the game is closed/terminated

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # create screen
    screen.fill(Colors().get_white())
    pygame.display.set_caption("Battleship")

    while running:
        game = Game()
        game.update()
        #game.close()

    pygame.quit()