import pygame, sys   # importing pygame library
from settings import * # importing everything from settings file
from level import Level

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) # initiating pygame / creating a display surface and clock
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level() # creating an instance of level class

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # event loop checking if we are closing the game
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update() # updating the screen, color black and setting fps
            self.clock.tick(FPS)

if __name__ == '__main__':  # first check if this the main file
    game = Game() # creating an instance of our game class
    game.run() # method run of the class
