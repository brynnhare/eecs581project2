# interface and other elements (buttons, menus, etc)
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

# fonts -- just a default font for now
FONT = pygame.font.Font(pygame.font.get_default_font(), 24)

class Board:
    def __init__(self, WIDTH, HEIGHT, board_name):
        self.board_name = board_name
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.rows = 11
        self.cols = 11
        self.square_size = WIDTH // 20
        self.surface = pygame.Surface((self.cols * self.square_size, self.rows * self.square_size))  # create the board as a pygame surface

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.surface, BLUE, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size), 1)

    def draw_labels(self):
        # Row numbers (1-10)
        for row in range(1, self.rows+1):
            label = FONT.render(str(row + 1), True, BLACK)
            self.surface.blit(label, (5, row * self.square_size + self.square_size // 3 + 50))
        
        # Column letters (A-J)
        for col in range(1, self.cols+1):
            label = FONT.render(chr(64 + col), True, BLACK)
            self.surface.blit(label, (col * self.square_size + self.square_size // 3, 5 + 50))

    def draw(self):
        self.surface.fill(WHITE) # clear the surface before drawing

        label = FONT.render(self.board_name, True, (0, 0, 0))
        self.surface.blit(label, (self.WIDTH // 4, 10))
        self.draw_grid()
        self.draw_labels()

class Ships:
    def __init__(self, surface, square_size):
        """
        This class is used to draw ships on the board and remove them
        """
        self.surface = surface
        self.square_size = square_size

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
        return [(col, row)]

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
            return [(col, row), (col + 1, row)]
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 2))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 2), 3)
            return [(col, row), (col, row + 1)]
    
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
            return [(col, row), (col + 1, row), (col + 2, row)]
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 3))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 3), 3)
            return [(col, row), (col, row + 1), (col, row + 2)]
    
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
            return [(col, row), (col + 1, row), (col + 2, row), (col + 3, row)]
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 4))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 4), 1)
            return [(col, row), (col, row + 1), (col, row + 2), (col, row + 3)]
    
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
            return [(col, row), (col + 1, row), (col + 2, row), (col + 3, row), (col + 4, row)]
        elif orientation == "vertical":
            pygame.draw.rect(self.surface, BLACK, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 5))
            pygame.draw.rect(self.surface, GREEN, (col * self.square_size, row * self.square_size + 50, self.square_size, self.square_size * 5), 3)
            return [(col, row), (col, row + 1), (col, row + 2), (col, row + 3), (col, row + 4)]
    
    def remove_ship(self, ship):
        """ 
        Removes a ship from the board.
        ship: list of tuples representing the squares the ship occupies (see return value of get_1x1, get_1x2, etc.)
        """
        for col, row in ship:
            # Convert (col, row) back to pixel positions
            x = col * self.square_size
            y = row * self.square_size + 50

            # Fill the grid square with the board background color (white in this case)
            pygame.draw.rect(self.surface, Colors().get_white(), (x, y, self.square_size, self.square_size))

            # Redraw the grid lines for the erased cell
            pygame.draw.rect(self.surface, Colors().get_blue(), (x, y, self.square_size, self.square_size), 1)
