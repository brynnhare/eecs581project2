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

import random # Use random library for AI opponent 
import os # used to clear the terminal screen in between turns

player1 = 1 #global variable to represent player 1
player2 = 2 #global variable to represent player 2
p1_misses = 0 #global variable to represent player 1 misses on p2 board
p1_hits = 0 #global variable to represent player 1 hits on p2 board
p1_sunk = 0 #global variable to represent player 1 ships sunk on p2 board
p2_misses = 0 #global variable to represent player 2 misses on p1 board
p2_hits = 0 #global variable to represent player 2 hits on p1 board
p2_sunk = 0 #global variable to represent player 2 ships sunk on p1 board

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
        """
        print out the key so that the reader can understand the symbols
        """
        print("Symbol Key for Battleship: ")
        print(f'\tShip: 0\n\tShip hit: X\n\tShip sunk: *\n\tOpen spot: ~\n\tMissfire: .\n')

    def display_board(self): 
        """
        disply the current users board
        Display columns denoted A-J
        """
        print("Here is your board: ")
        print() #add a leading space for the board
        print(" ".join(chr(ord('A') + i) for i in range(10))) # print out letters as column headers

        # Display rows denoted 1-10
        for i, row in enumerate(self.board):
            # Check each element in the row, replace int with "O", else leave as is
            formatted_row = ["O" if isinstance(cell, int) else cell for cell in row] # if there is an int, meaning a ship, just print out an "O" for easier readability
            print(" ".join(formatted_row) + f" {i + 1}") # join together all characters in a row seperated by a space, and followed by the row number

    def display_opponent_board(self): 
        """
        printing out your opponents board, not displaying their unhit ships
        """
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
        """
        Check if spot is free for use in ship placement
        """
        if self.board[row][column] == "~": # if there is not a ship placed yet
            return True
        else:
            print("You have already guessed that spot. Please try again.") # if there is a ship there, let the user know
            return False #already a ship in that spot

    def is_valid(self, row, column):
        """
        Check if spot is valid (spot is empty and within range)
        """
        if row <= 10 and column <= 10 and self.is_empty(row, column): # checking if spot is within range and then if it is empty
            return True
        else:
            return False 
        
    def place_ships(self, ship): 
        """
        add the ships into the board
        ship will be a size array of two ints (ex [1,2])
        """
        print("Ship size: ", ship[1]) # let the user know the ship they are placing
        orientation = "none" # forcing the player to select a boat orientation each round
        if (ship[1] == 1) and (ship[0] == 1): #if the ship is of size 1
            orientation = "h" #don't prompt the user for orientation
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
                        location[1] = 99 #sets the location to 99 because it is an invalid location. Once it reaches the check at line 107, it will be invalid.
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
        """
        make guess, check if guess is valid and then update board
        return 0 for miss, 1 for hit, and 2 for a sink
        """
        if len(guess_coordinate) == 3:
            guess_coordinate = list(guess_coordinate) # store as list
            guess_coordinate[1] = 10
        else:
            guess_coordinate = list(guess_coordinate) # store as list
            guess_coordinate[1] = int(guess_coordinate[1])
        
        target_value = self.board[int(guess_coordinate[1])-1][ord(guess_coordinate[0].lower()) - 97]

        if target_value == "." or target_value == "X": # if the spot has already been guessed
            print("You have already guessed that spot. Please try again.")
            return 3

        if isinstance(target_value, int): # is a ship
            """
            TODO: the logic below will give an IndexError: list index out of range if A1 is guessed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """
            ship.remaining_units[target_value-1] = ship.remaining_units[target_value-1] -1 # if so decrement for a hit
            self.board[guess_coordinate[1]-1][ord(guess_coordinate[0].lower()) - 97] = "X" #mark board with an X
            if ship.remaining_units[target_value-1] == 0: # ship is sunk
                return 2
            else:
                return 1 # hit but no sink
        else:
            self.board[guess_coordinate[1]-1][ord(guess_coordinate[0].lower()) - 97] = "." #mark board with a . 
            return 0


    def game_over(self):
        """
        return true if the board has no more unsunk ships, false otherwise
        """
        for rows in self.board:
            for space in rows:
                if isinstance(space, int):
                    return False
        return True
    
    def ai_place_ships(self, ship_types):
        occupied_spots = [] # Initialize list for occupied spots
        # Place each of the player's ships
        for ship in ship_types:
            # TODO: Implement actual autonomous ship placement
            
            orientation = random.choice(["h", "v"]) # Randomly select if orientation is horizontal or vertical 
            if ship[0] == 1: #if ship is horizontal, the other dimension will be the ship size
                ship_num = ship[1] # keeping track of the ship size as the ship number for use in sink detection
            else:
                ship_num = ship[0]
            if orientation == "v": # Swap ship coordinates if vertical 
                temp = ship[0]
                ship[0] = ship[1]
                ship[1] == temp
            invalid = True
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            while invalid: 
                letter = random.choice(letters[:len(letters)-ship_num + 1]) # Randomly select column with bounds
                number = random.choice(numbers[:len(numbers)-ship_num + 1]) # Randomly select row with bounds
                #the following section prevents placing a ship on a ship that is already there
                for i in range(0,ship_num+1):
                    if orientation == "v":
                        if [(ord(letter) -97), number + i] not in occupied_spots:
                            invalid = False
                        else:
                            invalid = True 
                            break
                    if orientation == "h":
                        if [(ord(letter) -97) + i, number] not in occupied_spots:
                            invalid = False
                        else:
                            invalid = True 
                            break
            location = [letter,number] # Location is random row and column together to form coordinate          



                

        # TO DO: Checking if AI ship's placing is valid 
        # To check if AI player's ship placement is valid (within bounds and no overlap):
        #   Initialize empty list that will store where a ship segment is on the board
        #   After placing the first ship for the AI's board (size 1 default), record the coordinate that is now occupied
        #   Then, when next ship (size 2) is being placed:
        #       AI will randomly generate a coordinate
        #       If the ship was VERTICAL:
        #           Check if selected coordinate and coordinate BELOW are within bounds and unoccupied
        #       If the ship was HORIZONTAL:
        #           Check if selected coordinate and coordinate to its RIGHT are within bounds and unoccupied 
        #   Repeat for proceeding sizes (size 3 checks next 2 coordinates below/right, size 4 checks next 3 coordinates below/right, size 5 checks next 4 coordinates below/right)
 
            if ship[0] == 1: #horizontal?
                ship_size = ship[1]
                for i in range(ship[1]): # add a mark for each of the ship units
                    if self.is_valid((location[1]-1),(ord(location[0].lower()) - 97)):
                        self.board[location[1]-1][ord(location[0].lower()) - 97] = ship_size
                        occupied_spots.append([(ord(location[0].lower()))-97, (location[1]-1)]) #format of letter, number (letter is in number form though)
                        location[0] = chr(ord(location[0]) + 1)

                    else: 
                        for row in range(10):
                            for col in range(10):
                                if self.board[row][col] == ship_num:
                                    self.board[row][col] = "~"
                          

            else: #vertical?
                ship_size = ship[0]
                for i in range(ship[0]): # add a mark for each of the ship units
                    if self.is_valid((location[1]-1),(ord(location[0].lower()) - 97)):
                        self.board[location[1]-1][ord(location[0].lower()) - 97] = ship_size
                        occupied_spots.append([(ord(location[0].lower()))-97, (location[1]-1)]) #format of letter, number (letter is in number form though)
                        location[1] = location[1]+1
                    else:
                        for row in range(10):
                            for col in range(10):
                                if self.board[row][col] == ship_num:
                                    self.board[row][col] = "~"


class Ships: 
    """
    class that handles 1b; assigning the correct number of ships to a user
    """
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
    """
    Can be used any time to switch players
    The main purpose of this class is to give the players a warning that a turn will switch 
    This prevents the opposing player's board from displaying, spoiling the secrecy of the game
    """
    def __init__(self):
        """
        Initialize player by starting with player 1 
        """
        self.player_num = 1
    
    def change(self):
        """
        To change players
        """
        if self.player_num == 1: 
            self.player_num = 2 # If currently player 1, switch to player 2
        else: 
            self.player_num = 1 # If currently player 2, switch to player 1 
            
    # To begin player's turn 
    def begin_turn(self):
        """
        Begin player's turn and wait until there is an input
        """
        print("Begin Player", self.player_num,"'s Turn (Press Enter)") 
        input() # Requires user to enter to confirm start of a turn 
        
    def end_turn(self):
        """
        To end player's turn 
        Display turn is ending for the player and wait until there is an input
        """
        print("End Player", self.player_num,"'s Turn (Press Enter)") 
        input() # Requires user to enter to confirm end of their turn 

        # Switch players after confirming turn is over 
        self.change() 
        clear_terminal() # Clear the terminal screen after each turn

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal screen after each turn

def is_valid_coordinate(coordinate):
    """
    Check if coordinate is valid 
    Check if coordinate has correct number of characters 
    """
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

def two_player_game():
    # Initialize the boards, ships, and players
    global p1_misses #make the global variable useable 
    global p1_hits #make the global variable useable 
    global p1_sunk #make the global variable useable 
    global p2_misses #make the global variable useable 
    global p2_hits #make the global variable useable 
    global p2_sunk #make the global variable useable 
    boards = [Board(player1), Board(player2)] # Store boards in an array to access easier
    ships = [Ships(player1), Ships(player2)] # Store ships in an array 
    currentplayer = SwitchPlayers() # Object that controls who the current player is

    # Start game
    startGame = Game(boards, ships, currentplayer)

    # Set up board for player 1
    startGame.human_game_setup(0)

    # Set up board for player 2
    startGame.human_game_setup(1)

    # Main game loop to be repeated until there is a winner
    gameOver = False # Flag for if game is over (initialize to False)
    player_continue = True # Flag for if player's turn is still active (initialize to True)

    # Loop until game is over 
    while not gameOver:
        player_continue = True
        currentplayer.begin_turn() # Start the next turn
        scoreboard()

        # Keep track of boards
        currentboard = currentplayer.player_num - 1 # Keep track of current player's board
        if currentboard == 0: # Keep track of the opponents board
            opponentboard = 1
        else:
            opponentboard = 0

        # For current player to take turn and fire 
        boards[currentboard].display_board() # Display current player's board
        while player_continue: 
            boards[opponentboard].display_opponent_board() # Display their opponents board

            # Guess coordinate to fire 
            while True:
                guess_coordinate = input("Input the coordinate you want to fire at (e.g., A5 or A10): ").upper()
                if is_valid_coordinate(guess_coordinate):
                    fire = boards[opponentboard].fire(guess_coordinate, ships[opponentboard]) # Fire and store output
                    if fire == 3:
                        continue
                    break  # Exit the loop if coordinate user chose is valid 
                # Prompt until valid coordinate is inputted 
                else:
                    print("Invalid coordinate! Please enter a valid coordinate (e.g., A5 or A10).") 

            # MISS
            if fire == 0: # If output is 0, it's a MISS
                print("MISS")
                if currentplayer.player_num == 1: #adjust scoreboard
                    p1_misses += 1 #adjust scoreboard
                if currentplayer.player_num == 2:#adjust scoreboard
                    p2_misses += 1 #adjust scoreboard
                boards[opponentboard].display_opponent_board() # Display board after miss
                player_continue = False # Break loop for next player by changing flag
                scoreboard()
                currentplayer.end_turn() # End turn
            # HIT
            elif fire == 1: # If output is 1, it's a HIT
                print("HIT") # If hit, continue in loop for player to continue turn 
                if currentplayer.player_num == 1: #adjust scoreboard
                    p1_hits += 1 #adjust scoreboard
                if currentplayer.player_num == 2: #adjust scoreboard
                    p2_hits += 1 #adjust scoreboard
            # Sinking a battleship 
            else:
                print("SUNK BATTLESHIP") # If 2 is returned, ship is sunk
                if currentplayer.player_num == 1:  #adjust scoreboard
                    p1_hits += 1 #adjust scoreboard
                    p1_sunk += 1 #adjust scoreboard
                if currentplayer.player_num == 2: #adjust scoreboard
                    p2_hits += 1 #adjust scoreboard
                    p2_sunk += 1 #adjust scoreboard
                if boards[opponentboard].game_over():
                    print(f"GAME OVER: Player {currentplayer.player_num} wins!")
                    gameOver = True # Mark game as over using flag
                    scoreboard()
                    break


class AIOpponent:
    def __init__(self):
        pass

    def fire_easy(self, board, ship):
        """
        Fire at random coordinates on the board
        return 0 for miss, 1 for hit, and 2 for a sink
        """
        # generate random coordinates
        letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) # Randomly select column
        number = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']) # Randomly select row 
        guess_coordinate = letter + number # Location is random row and column together to form coordinate
        try:
            fire = board.fire(guess_coordinate, ship) # Fire at random coordinate
        except:
            return self.fire_easy(board, ship)
        print(f"AI fires at {guess_coordinate.upper()}!")
        return fire # Return AI's guess and result of firing

    def fire_medium(self): 
        """
        Fire at random coordinates until a ship is hit, then hit orthogonally adjacent until ship is sunk
        return 0 for miss, 1 for hit, and 2 for a sink
        """
        pass

    def fire_hard(self): 
        """
        Fire at all coordinates that contain a ship
        This function should recusively fire at all coordinates that contain a ship until the entire ship is sunk
        return 2 for a sink, since all hits will be hits
        """
        pass


def one_player_game():
    while True:
        difficulty = int(input("Do you want an easy(1), medium(2), or hard(3) opponent? "))
        if difficulty == 1 or difficulty == 2 or difficulty == 3:
            break
        else:
            print("Invalid difficulty. Please enter 1, 2, or 3.")

    # Initialize the boards, ships, and players
    boards = [Board(player1), Board(player2)] # Store boards in an array to access easier
    ships = [Ships(player1), Ships(player2)] # Store ships in an array 
    currentplayer = SwitchPlayers() # Object that controls who the current player is
    aiplayer = AIOpponent()

    # Start game
    startGame = Game(boards, ships, currentplayer)

    # Set up board for player 1
    startGame.human_game_setup(0)

    # Set up board for ai player
    startGame.ai_game_setup(1)

    # Main game loop to be repeated until there is a winner
    gameOver = False # Flag for if game is over (initialize to False)
    player_continue = True # Flag for if player's turn is still active (initialize to True)

    # Loop until game is over 
    while not gameOver:
        player_continue = True
        # Keep track of boards
        currentboard = currentplayer.player_num - 1 # Keep track of current player's board
        if currentboard == 0: # Keep track of the opponents board
            opponentboard = 1
        else:
            opponentboard = 0
        
        while player_continue: 
            if currentplayer.player_num == 1: # if it is the real person
                # currentplayer.begin_turn() # Start the next turn
                print("It is your turn")
                # For current player to take turn and fire 
                boards[currentboard].display_board() # Display current player's board
                boards[opponentboard].display_opponent_board() # Display their opponents board

                # Guess coordinate to fire 
                while True:
                    guess_coordinate = input("Input the coordinate you want to fire at (e.g., A5 or A10): ").upper()
                    if is_valid_coordinate(guess_coordinate):
                        fire = boards[opponentboard].fire(guess_coordinate, ships[opponentboard]) # Fire and store output
                        if fire == 3:
                            continue
                        break  # Exit the loop if coordinate user chose is valid 
                    # Prompt until valid coordinate is inputted 
                    else:
                        print("Invalid coordinate! Please enter a valid coordinate (e.g., A5 or A10).") 

            if currentplayer.player_num == 2:
                if difficulty == 1:
                    fire = aiplayer.fire_easy(boards[opponentboard], ships[opponentboard])
                elif difficulty == 2:
                    fire = aiplayer.fire_medium()
                else:
                    fire = aiplayer.fire_hard()
            # MISS
            if fire == 0: # If output is 0, it's a MISS
                player_continue = False # Break loop for next player by changing flag
                if currentplayer.player_num == 1:
                    print("MISS")
                    boards[opponentboard].display_opponent_board() # Display board after miss
                    currentplayer.end_turn() # End turn
                else:
                    print("End of AI player's turn")
                    currentplayer.change()

            # HIT
            elif fire == 1: # If output is 1, it's a HIT
                print("HIT") # If hit, continue in loop for player to continue turn 
            else:
                print("SUNK BATTLESHIP") # If 2 is returned, ship is sunk
                if boards[opponentboard].game_over():
                    print(f"GAME OVER: Player {currentplayer.player_num} wins!")
                    gameOver = True # Mark game as over using flag
                    break



class Game:
    def __init__(self, boards, ships, currentplayer):
        self.boards = boards # [Board(player1), Board(player2)]
        self.ships = ships # [Ships(player1), Ships(player2)]  
        self.currentplayer = currentplayer # SwitchPlayers() object

    def human_game_setup(self, player_num): 
        """
        Method where player sets up their board
        """

        # Prompt current player to begin first turn 
        self.currentplayer.begin_turn() 

        # Print the key & symbols for the games
        self.boards[player_num].symbol_key()

        # Prompt current player to select number of ships (1-5)
        self.ships[player_num].choose_ships() 
        self.ships[player_num].load_types() # Create the list to store current player's ships
        
        # Display the blank board
        self.boards[player_num].display_board() 

        # Place each of the player's ships 
        for ship in self.ships[player_num].ship_types: # Iterate over list of ships to place each ship the player has
            self.boards[player_num].place_ships(ship) # Make the board class write in the ship to the board as its placed
            self.boards[player_num].display_board() # Display what the updated board looks like after a ship is placed 
        
        # Confirm the end of current player's setup turn and make opponent the new current player
        self.currentplayer.end_turn() 
    
    def ai_game_setup(self, player_num):
        """
        Method where AI sets up their board
        TODO: implement actual autonomous ship placement, because right now it's just manual placement based on the other player's board
        """
        print("AI is setting up their board...")
        self.ships[player_num].num_ships = self.ships[player_num - 1].num_ships # Get the number of ships the AI will have from the other player's setup
        ship_types = self.ships[player_num - 1].ship_types # Get the ship types the AI will have from the other player's setup

        self.boards[player_num].ai_place_ships(ship_types)
        self.boards[player_num].display_board()     #testing print

        self.currentplayer.end_turn()

def scoreboard(): #function to display the scoreboard
    board = (f' __________ __________\n'
            f'| Player 1 | Player 2 |\n'
            f'|__________|__________|\n'
            f'|Misses: {p1_misses} |Misses {p2_misses}  |\n'
            f'|Hits: {p1_hits}   |Hits {p2_hits}    |\n'
            f'|Sinks: {p1_sunk}  |Sinks: {p2_sunk}  |\n'
            f'|__________|__________|\n')
    print(board) #print the board


if __name__ == '__main__':
    # ask if it will be a two player game or an ai game
    while True:
        player_count = int(input("How many players do you have: "))
        if player_count == 2:
            two_player_game()
            break
        if player_count == 1:
            one_player_game()
            break
        else:
            print("Invalid number of players. Please enter 1 or 2.")
    



