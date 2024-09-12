#! python3
# game loop and  all core logic
'''
Program: Battleship
Description: This program will be a functional two player game of battleship. This
    file contains the main game loop and core logic.
Output: A game of battleship played in the terminal.
Authors: Brynn Hare, Micah Borghese, Katelyn Accola, Nora Manolescu, and Kyle Johnson
Creation date: 9/4/2024
'''

player1 = 1
player2 = 2

class Board: 
    def __init__(self, player_num):
        self.player_num = player_num # Assign each player number a corresponding board
        self.board = [["~" for _ in range(10)] for _ in range(10)] # upon creation, game board should be filled with empty spaces only

        # Key: 
        # Ship: O (store ship as their ship number(ex 1) to keep track of when a ship is sunk, but print out O )
        # Ship hit: X
        # Ship sunk: *
        # Open spot: ~
        # Missfire: .
    
    def symbol_key(self): 
        # print out the key so that the reader can understand the symbols
        print("Symbol Key for Battleship: ")
        print(f'\tShip: 0\n\tShip hit: X\n\tShip sunk: *\n\tOpen spot: ~\n\tMissfire: .\n')

    def display_board(self): 
        # disply the current users board
        # Display columns denoted A-J
        print("Here is your board: ")
        print() #add a leading space for the board
        print(" ".join(chr(ord('A') + i) for i in range(10))) # print out letters as column headers

        # Display rows denoted 1-10
        for i, row in enumerate(self.board):
            # Check each element in the row, replace int with "O", else leave as is
            formatted_row = ["O" if isinstance(cell, int) else cell for cell in row] # if there is an int, meaning a ship, just print out an "O" for easier readability
            print(" ".join(formatted_row) + f" {i + 1}") # join together all characters in a row seperated by a space, and followed by the row number

    def display_opponent_board(self): 
        # printing out your opponents board, not displaying their unhit ships
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
        # Check if spot is free for use in ship placement
        if self.board[row][column] == "~": # if there is not a ship placed yet
            return True
        else:
            return False #already a ship in that spot

    def is_valid(self, row, column):
        # Check if spot is valid (spot is empty and within range)
        if row <= 10 and column <= 10 and self.is_empty(row, column): # checking if spot is within range and then if it is empty
            return True
        else:
            return False 

    def place_ships(self, ship): 
        #add the ships into the board
        # ship will be a size array of two ints (ex [1,2])
        print("Ship size: ", ship[1]) # let the user know the ship they are placing
        orientation = "none" # forcing the player to select a boat orientation each round
        if ship[0] == 1: #if ship is horizontal, the other dimension will be the ship size
            ship_num = ship[1] # keeping track of the ship size as the ship number for use in sink detection
        else:
            ship_num = ship[0]
        while (orientation != "h") and (orientation != "v"): #continue to ask for the ship orientation if not answered with an h or v
            orientation_input = input("Would you like your ship to be horizontal or vertical?\nEnter 'h' for horizontal. Enter 'v' for vertical.\n") #prompt user for orientation
            orientation = orientation_input.lower() #make the user input lowercase
            if orientation == "v": #swap ship coordinates if verticle to 
                temp = ship[0]
                ship[0] = ship[1]
                ship[1] == temp
        invalid_location = True #variable to keep track of location validity
        while invalid_location: #while the location is invalid
            try: 
                location = input("Enter the upper leftmost coordinate you would like your ship to be placed at: ") #location will be a string for ex A1
                location = list(location) #store as an array 
                if len(location) > 3:
                    location[1] = 99 # change to 99 to ensure it will be marked as invalid in checks below
                elif len(location) == 3: #if the length is three than the value must be 10 (otherwise out of range..)
                    if int(location[2]) == 0: # store the number value in the index 1 if it is a 10
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
            try: 
                if ship[0] == 1: #horizontal?
                    ship_size = ship[1]
                    for i in range(ship[1]): # add a mark for each of the ship units
                        if self.is_valid((location[1]-1),(ord(location[0].lower()) - 97)):
                            self.board[location[1]-1][ord(location[0].lower()) - 97] = ship_size
                            location[0] = chr(ord(location[0]) + 1)
                        else: 
                            for row in range(10):
                                for col in range(10):
                                    if self.board[row][col] == ship_num:
                                        self.board[row][col] = "~"
                            raise Exception("invalid loction")

                else: #vertical?
                    ship_size = ship[0]
                    for i in range(ship[0]): # add a mark for each of the ship units
                        if self.is_valid((location[1]-1),(ord(location[0].lower()) - 97)):
                            self.board[location[1]-1][ord(location[0].lower()) - 97] = ship_size
                            location[1] = location[1]+1
                        else:
                            for row in range(10):
                                for col in range(10):
                                    if self.board[row][col] == ship_num:
                                        self.board[row][col] = "~"
                            raise Exception("invalid loction")
                invalid_location = False
            except: 
                print("That location is not valid")

    

    def fire(self, guess_coordinate, ship):
        #make guess, check if guess is valid and then update board
        # return 0 for miss, 1 for hit, and 2 for a sink
        if len(guess_coordinate) == 3:
            guess_coordinate = list(guess_coordinate) # store as list
            guess_coordinate[1] = 10
        else:
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
    # Can be used any time to switch players
    # The main purpose of this class is to give the players a warning that a turn will switch 
    # This prevents the opposing player's board from displaying, spoiling the secrecy of the game
    def __init__(self):
        # Initialize player by starting with player 1 
        self.player_num = 1
    
    # To change players
    def change(self):
        if self.player_num == 1: 
            self.player_num = 2 # If currently player 1, switch to player 2
        else: 
            self.player_num = 1 # If currently player 2, switch to player 1 
            
    # To begin player's turn 
    def begin_turn(self):
        # Begin player's turn and wait until there is an input
        print("Begin Player", self.player_num,"'s Turn (Press Enter)") 
        input() # Requires user to enter to confirm start of a turn 
        
    # To end player's turn 
    def end_turn(self):
        # Display turn is ending for the player and wait until there is an input
        print("End Player", self.player_num,"'s Turn (Press Enter)") 
        input() # Requires user to enter to confirm end of their turn 

        # Switch players after confirming turn is over 
        self.change() 

# Check if coordinate is valid 
def is_valid_coordinate(coordinate):
    # Check if coordinate has correct number of characters 
    if len(coordinate) < 2 or len(coordinate) > 3:
        return False

    # Store coordinate row and column 
    row = coordinate[0].upper()
    col = coordinate[1:]

    # Check if the row is a letter between A and J (for a 10x10 grid)
    if row < 'A' or row > 'J':
        return False

    # Check if the column is a number between 1 and 10
    if not col.isdigit() or not (1 <= int(col) <= 10):
        return False

    # Otherwise, coordinate is valid 
    return True

class Game:
    def __init__(self, boards, ships, currentplayer):
        self.boards = boards
        self.ships = ships
        self.currentplayer = currentplayer

    # Method where player sets up their board
    def game_setup(self, player): 
        # Prompt current player to begin first turn 
        self.currentplayer.begin_turn() 

        # Print the key & symbols for the games
        self.boards[player].symbol_key()

        # Prompt current player to select number of ships (1-5)
        self.ships[player].choose_ships() 
        self.ships[player].load_types() # Create the list to store current player's ships
        
        # Display the blank board
        self.boards[player].display_board() 

        # Place each of the player's ships 
        for ship in self.ships[player].ship_types: # Iterate over list of ships to place each ship the player has
            self.boards[player].place_ships(ship) # Make the board class write in the ship to the board as its placed
            self.boards[player].display_board() # Display what the updated board looks like after a ship is placed 
        
        # Confirm the end of current player's setup turn and make opponent the new current player
        self.currentplayer.end_turn() 


if __name__ == '__main__':

    # Initialize the boards, ships, and players
    boards = [Board(player1), Board(player2)] # Store boards in an array to access easier
    ships = [Ships(player1), Ships(player2)] # Store ships in an array 
    currentplayer = SwitchPlayers() # Object that controls who the current player is

    # Start game
    startGame = Game(boards, ships, currentplayer)

    # Set up board for player 1
    startGame.game_setup(0)

    # Set up board for player 2
    startGame.game_setup(1)

    # Main game loop to be repeated until there is a winner
    gameOver = False 
    player_continue = True
    while not gameOver:
        player_continue = True
        currentplayer.begin_turn() # start the next turn
        currentboard = currentplayer.player_num -1 # keep track of which board we are looking at
        if currentboard == 0: # also keep track of the opponents board
            opponentboard = 1
        else:
            opponentboard = 0
        boards[currentboard].display_board() # display their own board to see what opponent has hit
        while player_continue: 
            boards[opponentboard].display_opponent_board() # display their opponents board
            while True:
                guess_coordinate = input("Input the coordinate you want to fire at (e.g., A5 or A10): ").upper()
                if is_valid_coordinate(guess_coordinate):
                    break  # Exit the loop if input is valid
                else:
                    print("Invalid coordinate! Please enter a valid coordinate (e.g., A5 or A10).")
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





