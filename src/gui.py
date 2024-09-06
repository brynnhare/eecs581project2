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
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.rows = 10
        self.cols = 10
        self.square_size = 60

    # Draw grid on the board
    def draw_grid(self, screen):
        for row in range(self.rows + 1):
            for col in range(self.cols + 1):
                pygame.draw.rect(screen, BLUE, (col * self.square_size, row * self.square_size, self.square_size, self.square_size), 1)

    # Add labels (numbers for rows, letters for columns)
    def draw_labels(self, screen):
        # Row numbers (1-10)
        for row in range(1, self.rows+1):
            label = FONT.render(str(row), True, BLACK)
            screen.blit(label, (5, row * self.square_size + self.square_size // 3))
        
        # Column letters (A-J)
        for col in range(1, self.cols+1):
            label = FONT.render(chr(64 + col), True, BLACK)
            screen.blit(label, (col * self.square_size + self.square_size // 3, 5))

    # Combine grid and labels into one draw function
    def draw(self, screen):
        self.draw_grid(screen)
        self.draw_labels(screen)