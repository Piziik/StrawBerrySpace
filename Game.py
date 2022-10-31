##Impport all in settings file
import pygame

import settings
from settings import *

##Game class
class Game:
    ##Constructor
    def __init__(self):
        ##Init pygame library
        pygame.init()
        ##Create a window for the game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        ##Change the window's caption
        pygame.display.set_caption('StrawBerrySpace - Adventure')

    ##Run method (keeps the game open)
    def run(self):
        ##The game loop
        while True:
            ##Method located in settings.py
            ScrollBackground(self)

            ##Display player
            self.screen.blit(playerImage, (settings.playerX, settings.playerY))

            pressed = pygame.key.get_pressed()
            ##Quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            ##Move player
            if pressed[pygame.K_LEFT]:
                settings.playerX -= 15
                if settings.playerX <= 0:
                    settings.playerX = 0
            if pressed[pygame.K_RIGHT]:
                settings.playerX += 15
                if settings.playerX >= (self.screen.get_width() - 45):
                    settings.playerX = self.screen.get_width() - 45

            ##Update display
            pygame.display.update()