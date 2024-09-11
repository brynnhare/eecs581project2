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

        # Ship: O (store ship as their ship number(ex 1) to keep track of when a ship is sunk, but print out O )
        # Ship hit: X
        # Ship sunk: *
        # Open spot: ~
        # Missfire: .

    def display_board(self):
        # Display columns denoted A-J
        print("Here is your board: ")
        print() #add a leading space for the board
        print(" ".join(chr(ord('A') + i) for i in range(10)))

        # Display rows denoted 1-10
        for i, row in enumerate(self.board):
            # Check each element in the row, replace int with "O", else leave as is
            formatted_row = ["O" if isinstance(cell, int) else cell for cell in row]
            print(" ".join(formatted_row) + f" {i + 1}")

    def display_opponent_board(self): # currently is printing the row nums on the opposite side as the display_board, not sure which one we want but should probably be the same
        print("Here is your opponents board: ")
        # To display the opponent's board, only showing the sunk ships (replace unsunk ships with '~')
        # Display columns denoted A-J
        print()  # Add a leading space for the board
        print("  " + " ".join(chr(ord('A') + i) for i in range(10)))  # Column labels A-J with space before them
        
        # Display rows denoted 1-10
        for i, row in enumerate(self.board):
            # Replace non-sunk ships with '~'
            display_row = ['~' if isinstance(cell, int) else cell for cell in row] # dont print where opponents ships are
            # Print the row with the row number
            print(f"{i + 1:2} " + " ".join(display_row))  # Row number with space and row content
            
        print()  # Add a trailing space for the board

    def is_empty(self, row, column):
        # Check if spot is free
        if self.board[row][column] == "~":
            return True
        else:
            return False 

    def is_valid(self, row, column):
        # Check if spot is valid (spot is empty and within range)
        if row <= 10 and column <= 10 and self.is_empty(row, column):
            return True
        else:
            return False 

    def place_ships(self, ship): # ship needs to be an array of ints
        #add the ships into the board
        # ship will be a size array(ex [1,2])
        # we still need to add more error detection, such as if the ship will go out of bounds or overlap with another ship
        print("Ship size: ", ship[1])
        orientation = "none" # forcing the player to select a boat orientation each round
        while (orientation != "h") and (orientation != "v"): #continue to ask for the ship orientation if not answered with an h or v
            orientation_input = input("Would you like your ship to be horizontal or vertical?\nEnter 'h' for horizontal. Enter 'v' for vertical.\n") #prompt user for orientation
            orientation = orientation_input.lower() #make the user input lowercase
            if orientation == "v": #swap coordinates if verticle
                temp = ship[0]
                ship[0] = ship[1]
                ship[1] == temp
        invalid_location = True #variable to keep track of location validity
        while invalid_location: #while the location is invalid
            try: 
                location = input("Enter the upper leftmost coordinate you would like your ship to be placed at: ") #location will be a string for ex A1
                location = list(location) #store as an array 
                if len(location) > 3:
                    location[1] = 99
                elif len(location) == 3: #if the length is three than the value must be 10 (otherwise out of range..)
                    if int(location[2]) == 0: 
                        location[1] = 10 #make the location 10
                    else: 
                        location[1] = 99
                else:  #if it isn't that length it is normal
                    location[1]= int(location[1]) #cast the number as an int
                location[0] = location[0].lower() #make the letter value lowercase
                if (location[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) and (location[1] in range(1,11)): #check that the values are in the correct range
                    invalid_location = False #if they are, break the while loop
            except:
                invalid_location = True
        if ship[0] == 1: #horizontal?
            ship_size = ship[1]
            for i in range(ship[1]): # add a mark for each of the ship units
                self.board[location[1]-1][ord(location[0].lower()) - 97] = ship_size
                location[0] = chr(ord(location[0]) + 1)
        else: #vertical?
            ship_size = ship[0]
            for i in range(ship[0]): # add a mark for each of the ship units
                self.board[location[1]-1][ord(location[0].lower()) - 97] = ship_size
                location[1] = location[1]+1
    

    def fire(self, guess_coordinate, ship):
        #make guess, check if guess is valid and then update board
        # return 0 for miss, 1 for hit, and 2 for a sink
        guess_coordinate = list(guess_coordinate) # store as list
        guess_coordinate[1] = int(guess_coordinate[1])
        target_value = self.board[guess_coordinate[1]-1][ord(guess_coordinate[0].lower()) - 97]
        if isinstance(target_value, int): # is a ship)
            ship.remaining_units[target_value-1] = ship.remaining_units[target_value-1] -1 # if so decrement for a hit
            self.board[guess_coordinate[1]-1][ord(guess_coordinate[0].lower()) - 97] = "X" #mark board with an X
            if ship.remaining_units[target_value-1] == 0: # ship is sunk
                return 2
            else:
                return 1 # hit but no sink
        else:
            self.board[guess_coordinate[1]-1][ord(guess_coordinate[0].lower()) - 97] = "." #mark board with a . 
            return 0

        pass

    def game_over(self):
        # return true if the board has no more unsunk ships, false otherwise
        for rows in self.board:
            for space in rows:
                if isinstance(space, int):
                    return False
        return True


class Ships: 
    #class that handles 1b; assigning the correct number of ships to a user
    def __init__(self, player_num):
        self.player_num = player_num #this will be put in by us each time they switch, to reprsent player 1 or 2
        self.num_ships = 0 #this is provided by the player later (must be numbers 1-5 inclusively)
        self.ship_types = [] #empty list to hold the sizes of the ships
        self.remaining_units = [] #keep track of how many units of a ship have been hit to know when it is sunk

    def choose_ships(self): #the player must select the number of ships they want to have
        while True:    
            try:  
                num_ships = int(input("Choose the number of ships for your board (1-5): "))
                self.num_ships = num_ships
                break
            except: 
                print("Invalid number of ships.")
        while (self.num_ships < 1) or (self.num_ships > 5): #checking for invalid ship values
            try: 
                new_num = int(input("Invalid number of ships. Select a new number: ")) #prompt for another number ***THIS CAN BE CHANGED JUST AN INITIAL PHASE***
                self.num_ships = new_num #assign the new number to be the number of ships
            except: 
                self.num_ships = 0
        for i in range(num_ships): # keep track of how many unsunk units for each ship
            self.remaining_units.append(i+1)

    def load_types(self): #this forms the list with the sizes of the ships
        i = 1 #initializing for the while loop
        while i < (self.num_ships + 1): #while the current ship number is less than one extra than the number of ships chosen
            self.ship_types.append([1, i]) #append to the list. [1, 1] represents 1 x 1. [1, 2] represents 1 x 2...etc.
            i += 1 #increase the while loop



class SwitchPlayers:
    #this can be used anytime to move from player 1 to 2 
    #the main purpose of this class is to give the players a warning that a turn will switch. This prevents the opposing player's board from displaying, spoiling the secrecy of the game
    def __init__(self):
        self.player_num = 1 #initialized by starting with player 1
    
    def change(self):
        if self.player_num == 1:
            self.player_num = 2
        else: 
            self.player_num = 1
            
    def begin_turn(self):
        print("Begin Player", self.player_num,"'s Turn (Press Enter)") #Begins player turn waits till theres an input
        input() #require an enter to confirm the start of a turn
        
    def end_turn(self):
        print("End Player", self.player_num,"'s Turn (Press Enter)") #display that the turn is ending
        input() #require an enter to confirm ending a turn
        self.change() #switch players after the confirmation of a turn ending


def is_valid_coordinate(coordinate):
    if len(coordinate) < 2 or len(coordinate) > 3:
        return False

    row = coordinate[0].upper()
    col = coordinate[1:]

    # Check if the row is a letter between A and J (for a 10x10 grid)
    if row < 'A' or row > 'J':
        return False

    # Check if the column is a number between 1 and 10
    if not col.isdigit() or not (1 <= int(col) <= 10):
        return False

    return True

if __name__ == '__main__':
    #start the game and initialize the boards, ships, and players
    boards = [Board(player1), Board(player2)] # store boards in an array to access easier
    # board1 = Board(player1) #board1 represents player 1's board
    # board2 = Board(player2) #board2 represents player 2's board
    ships = [Ships(player1), Ships(player2)] # making ships an array as well
    #ships1 = Ships(player1) #create an ships class for player 1
    #ships2 = Ships(player2) #create an ships class for player 2
    currentplayer = SwitchPlayers() #object that controls who the current player is

    #begin the game setup for player1
    currentplayer.begin_turn() #prompt player 1 to begin first turn 
    ships[0].choose_ships() #prompt player 1 with the number of ships to select
    ships[0].load_types() #create the list of ships for player 1
    boards[0].display_board() #display the blank board
    for ship in ships[0].ship_types: #depending on the number of ships picked
        # ships1.place(boards[0]) #place the ships
        boards[0].place_ships(ship) #making the board class write in the ship to the board as its placed
        boards[0].display_board() #display the current state of the board after each ship placement
    currentplayer.end_turn() #confirm the end of player 1's setup turn and make player 2 the new current player


    #begin the game setup for player2
    currentplayer.begin_turn() #prompt play 2 to being first setup turn
    ships[1].choose_ships() #prompt player 2 with the number of ships to select
    ships[1].load_types() #create the list of ships for player 2
    boards[1].display_board() #display the blank board
    for ship in ships[1].ship_types: #depending on the number of ships picked
        boards[1].place_ships(ship) #place the ships
        boards[1].display_board() #display the current state of the board after each ship placement
    currentplayer.end_turn() #end player 2's setup turn and make the current player player 1

    # main game loop to be repeated until there is a winner
    gameOver = False
    while not gameOver:
        currentplayer.begin_turn() # start the next turn
        currentboard = currentplayer.player_num -1 # keep track of which board we are looking at
        if currentboard == 0: # also keep track of the opponents board
            opponentboard = 1
        else:
            opponentboard = 0
        boards[currentboard].display_board() # display their own board to see what opponent has hit
        while True:
            guess_coordinate = input("Input the coordinate you want to fire at (e.g., A5 or A10): ").upper()
            if is_valid_coordinate(guess_coordinate):
                print(f"You fired at {guess_coordinate}")
                break  # Exit the loop if input is valid
    else:
        print("Invalid coordinate! Please enter a valid coordinate (e.g., A5 or A10).")
        while player_continue == True: 
            boards[opponentboard].display_opponent_board() # display their opponents board
            guess_coordinate = input("Input the coordinate you want to fire at ") # take in input as string, should add error detection
            fire = boards[opponentboard].fire(guess_coordinate, ships[opponentboard]) # fire and store output
            if fire == 0: # fire and if output is 0 its a miss
                print("MISS")
                boards[opponentboard].display_opponent_board() # after a miss display board
                player_continue = False # break loop for next player
                currentplayer.end_turn() #end turn
            elif fire == 1:
                print("HIT") # if hit, continue in loop
            else:
                print("SUNK BATTLESHIP") # if 2 is returned, ship is sunk
                if boards[opponentboard].game_over():
                    print(f"GAME OVER: Player {currentplayer.player_num} wins!")
                    gameOver = True
                    break


        
    





    
    
