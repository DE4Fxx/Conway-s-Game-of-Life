import pygame
import random

# Constants
HEIGHT, WIDTH = 1000, 1500
CELL_SIZE = 32
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class ConwayGame:
    __slots__ = ["screen", "clock", "running", "grid", "setup_mode"]

    def __init__(self, dimensions):
        pygame.init()
        self.screen = pygame.display.set_mode(dimensions)
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid = set()
        self.setup_mode = False  # Flag to check if we are in setup mode

    def start_screen(self):
        font = pygame.font.Font(None, 36)
        text = font.render('Press R for Random, M for Manual setup', True, WHITE)
        greeting = font.render('Welcome to Conway\'s game of life!', True, WHITE)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        greeting_rect= greeting.get_rect(center=(WIDTH//2,HEIGHT//4))

        while True:
            self.screen.fill(BLACK)
            self.screen.blit(text, text_rect)
            self.screen.blit(greeting, greeting_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.grid = set([(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if random.randint(0, 1)])
                        return
                    elif event.key == pygame.K_m:
                        self.setup_mode = True
                        return

    def draw_setup_message(self):
        font = pygame.font.Font(None, 36)  # Using a larger font for visibility
        message = "Press S to exit setup mode" if self.setup_mode else "Press S to enter setup mode"
        text = font.render(message, True, WHITE)

        # Position the text in the bottom-right corner
        text_x = self.screen.get_width() - text.get_width() - 10 
        text_y = self.screen.get_height() - text.get_height() - 10 

        self.screen.blit(text, (text_x, text_y))


    def clear_screen(self):
        self.grid = set()
        self.screen.fill(BLACK)



    def draw_clear_message(self):
        font = pygame.font.Font(None, 36)  # Using a larger font for visibility
        message = "Press C to clear the screen"
        text = font.render(message, True, WHITE)

        # Position the text in the bottom-right corner
        text_x = self.screen.get_width() - text.get_width() - 10 
        text_y = self.screen.get_height() - text.get_height() - 40 

        self.screen.blit(text, (text_x, text_y))


    def draw_grid(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = WHITE if (x, y) in self.grid else BLACK
                pygame.draw.rect(self.screen, color, rect)

    def update_grid(self):
        new_grid = set()
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                neighbors = sum((nx, ny) in self.grid for nx in range(x - 1, x + 2) for ny in range(y - 1, y + 2) if (nx, ny) != (x, y))
                if (x, y) in self.grid and neighbors in [2, 3]:
                    new_grid.add((x, y))
                elif (x, y) not in self.grid and neighbors == 3:
                    new_grid.add((x, y))
        self.grid = new_grid

    def run(self):
        self.start_screen()
        mouse_is_pressed = False
        while self.running:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.setup_mode = False if self.setup_mode == True else True
                    elif event.key == pygame.K_c:
                        self.clear_screen()

                if self.setup_mode:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_is_pressed = True
                        x, y = pygame.mouse.get_pos()
                        cell = (x // CELL_SIZE, y // CELL_SIZE)
                        self.grid.add(cell)  # Add cell on initial click
                    elif event.type == pygame.MOUSEBUTTONUP:
                        mouse_is_pressed = False
                    elif event.type == pygame.MOUSEMOTION and mouse_is_pressed:
                        x, y = event.pos
                        cell = (x // CELL_SIZE, y // CELL_SIZE)
                        self.grid.add(cell)  # Add cells while dragging


            if not self.setup_mode:
                self.update_grid()

            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_setup_message()
            self.draw_clear_message()
            pygame.display.flip()

        pygame.quit()

# Create and run the game
game = ConwayGame((WIDTH, HEIGHT))
game.run()