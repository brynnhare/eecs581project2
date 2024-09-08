# interface and other elements (buttons, menus, etc)
import pygame

pygame.init()

# colors -- can be changed to whatever
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

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

