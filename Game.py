##Import all in settings file
import settings
from settings import *
from Player import Player

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

            player = Player()

            ##Display player
            self.screen.blit(player.playerImage, (settings.playerX, settings.playerY))

            pressed = pygame.key.get_pressed()
            ##Quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            ##Move player
            if pressed[pygame.K_LEFT]:
                settings.playerX -= settings.playerVelocity
                if settings.playerX <= 0:
                    settings.playerX = 0
            if pressed[pygame.K_RIGHT]:
                settings.playerX += settings.playerVelocity
                if settings.playerX >= (self.screen.get_width() - PLAYER_HEIGHT):
                    settings.playerX = self.screen.get_width() - PLAYER_HEIGHT

            ##Update display
            pygame.display.update()