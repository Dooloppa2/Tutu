import pygame, sys
from window_settings import *

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Creating window
        pygame.display.set_caption("Tutu")  # Naming a window
        self.clock = pygame.time.Clock()  # Game timer for events


    def run(self):
        while True:
            for event in pygame.event.get():  # Getting events
                if event.type == pygame.QUIT:  # Closing window when clicking a cross
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')  # Cleaning everything from screen by filling it black
            pygame.display.update()  # Drawing everything
            self.clock.tick(FPS)  # Doing a single tick


if __name__ == '__main__':  # Work only when running as main
    game = Game()
    game.run()