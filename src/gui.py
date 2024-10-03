# interface and other elements (buttons, menus, etc)
"""
    This version of the game ultimately is not used in the final product.
"""
import pygame

pygame.init()

# colors -- can be changed to whatever
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Colors:
    def __init__(self):
        pass

    def get_white(self):
        return WHITE
    
    def get_black(self):
        return BLACK
    
    def get_blue(self):
        return BLUE

class Board:
    def __init__(self, WIDTH, HEIGHT, board_name):
        self.board_name = board_name
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.rows = 12
        self.cols = 11
        self.square_size = WIDTH // 20
        self.surface = pygame.Surface((self.cols * self.square_size, self.rows * self.square_size))  # create the board as a pygame surface
        self.cover_surface = pygame.Surface((self.cols * self.square_size, self.rows * self.square_size))
        self.FONT = pygame.font.Font(pygame.font.get_default_font(), 24) # fonts -- just a default font for now

    def show_text(self, text):
        """
        Displays text on the screen
        """
        label = self.FONT.render(text, True, BLACK)
        self.surface.blit(label, (self.WIDTH // 4, 100))
    
    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.surface, BLUE, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size), 1)

    def draw_labels(self):
        # Row numbers (1-10)
        for row in range(1, self.rows-1):
            label = self.FONT.render(str(row), True, BLACK)
            self.surface.blit(label, (5, row * self.square_size + self.square_size // 3 + 50))
        
        # Column letters (A-J)
        for col in range(1, self.cols+1):
            label = self.FONT.render(chr(64 + col), True, BLACK)
            self.surface.blit(label, (col * self.square_size + self.square_size // 3, 5 + 50))

    def draw(self):
        pygame.init()
        self.surface.fill(WHITE) # clear the surface before drawing

        label = self.FONT.render(self.board_name, True, (0, 0, 0))
        self.surface.blit(label, (self.WIDTH // 4, 10))
        self.draw_grid()
        self.draw_labels()

    def cover_board(self):
        self.cover_surface.fill(Colors().get_blue())

    def show_board(self):
        self.cover_surface.fill((0,0,0))

class Ships:
    def __init__(self, surface, square_size):
        """
        This class is used to draw ships on the board and remove them
        """
        self.surface = surface
        self.square_size = square_size
        self.cur_ships = []
    
    def is_valid(self, ship):
        """
        Checks whether a ship would be a valid placement on the board
        """
        for x, y in ship:
            if x <= "A" or y < 0 or x >= "J" or y >= 11:
                return False
        for otherShip in self.cur_ships:
            if self.ships_overlap(ship, otherShip):
                return False
        return True
    
    def ships_overlap(self, ship1, ship2):
        """
        Checks whether two ships have an overlap
        """
        for ship1_coord in ship1.coordinate_list:
            for ship2_coord in ship2.coordinate_list:
                if ship1_coord == ship2_coord:
                    return True
        return False

    def get_1x1(self, col, row):
        """
        col: string representing the column (A-J)
        row: integer representing the row (1-10)
        orientation: string representing the orientation of the ship ("horizontal" or "vertical")

        :return:
        A list of tuples representing the squares the ship
        """
        col = ord(col.upper()) - ord('A') + 1
        row -= 1
        pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size))
        pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size), 3)
        ship = [(col, row)]
        self.cur_ships.append(ship)
        return ship

    def get_1x2(self, col, row, orientation):
        """
        col: string representing the column (A-J)
        row: integer representing the row (1-10)
        orientation: string representing the orientation of the ship ("horizontal" or "vertical")

        :return:
        A list of tuples representing the squares the ship occupies
        """
        col = ord(col.upper()) - ord('A') + 1
        row -= 1
        if orientation == "horizontal":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size * 2, self.square_size))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size * 2, self.square_size), 3)
            ship = [(col, row), (col + 1, row)]
            self.cur_ships.append(ship)
            return ship
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 2))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 2), 3)
            ship = [(col, row), (col, row + 1)]
            self.cur_ships.append(ship)
            return ship
    
    def get_1x3(self, col, row, orientation):
        """
        col: string representing the column (A-J)
        row: integer representing the row (1-10)
        orientation: string representing the orientation of the ship ("horizontal" or "vertical")

        :return:
        A list of tuples representing the squares the ship occupies
        """
        col = ord(col.upper()) - ord('A') + 1
        row -= 1
        if orientation == "horizontal":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size * 3, self.square_size))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size * 3, self.square_size), 3)
            ship = [(col, row), (col + 1, row), (col + 2, row)]
            self.cur_ships.append(ship)
            return ship
        
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 3))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 3), 3)
            ship = [(col, row), (col, row + 1), (col, row + 2)]
            self.cur_ships.append(ship)
            return ship
    
    def get_1x4(self, col, row, orientation):
        """
        col: string representing the column (A-J)
        row: integer representing the row (1-10)
        orientation: string representing the orientation of the ship ("horizontal" or "vertical")

        :return:
        A list of tuples representing the squares the ship occupies
        """
        col = ord(col.upper()) - ord('A') + 1
        row -= 1
        if orientation == "horizontal":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size * 4, self.square_size))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size * 4, self.square_size), 3)
            ship = [(col, row), (col + 1, row), (col + 2, row), (col + 3, row)]
            self.cur_ships.append(ship)
            return ship
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 4))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 4), 1)
            ship = [(col, row), (col, row + 1), (col, row + 2), (col, row + 3)]
            self.cur_ships.append(ship)
            return ship
    
    def get_1x5(self, col, row, orientation):
        """
        col: string representing the column (A-J)
        row: integer representing the row (1-10)
        orientation: string representing the orientation of the ship ("horizontal" or "vertical")

        :return:
        A list of tuples representing the squares the ship occupies
        """
        col = ord(col.upper()) - ord('A') + 1
        row -= 1
        if orientation == "horizontal":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size * 5, self.square_size))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size * 5, self.square_size), 3)
            ship = [(col, row), (col + 1, row), (col + 2, row), (col + 3, row), (col + 4, row)]
            self.cur_ships.append(ship)
            return ship
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 5))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 5), 3)
            ship = [(col, row), (col, row + 1), (col, row + 2), (col, row + 3), (col, row + 4)]
            self.cur_ships.append(ship)
            return ship
    
    def remove_ship(self, ship):
        """ 
        Removes a ship from the board.
        ship: list of tuples representing the squares the ship occupies (see return value of get_1x1, get_1x2, etc.)
        """
        if ship in self.cur_ships:
            for col, row in ship:
                # Convert (col, row) back to pixel positions
                x = col * self.square_size
                y = row * self.square_size + 50

                # Fill the grid square with the board background color (white in this case)
                pygame.draw.rect(self.surface, Colors().get_white(), (x, y, self.square_size, self.square_size))

                # Redraw the grid lines for the erased cell
                pygame.draw.rect(self.surface, Colors().get_blue(), (x, y, self.square_size, self.square_size), 1)
        else:
            print("Ship not found!")
