from settings import *

class Player:
    def __init__(self):
        self.playerImage = pygame.image.load('assets/entity/ship.png')
        self.playerImage = pygame.transform.scale(self.playerImage, (PLAYER_HEIGHT, PLAYER_WIDTH))
