from settings import *
from Projectile import Projectile

class Player:
    def __init__(self):
        self.playerImage = pygame.image.load('assets/entity/ship.png')
        self.playerImage = pygame.transform.scale(self.playerImage, (PLAYER_HEIGHT, PLAYER_WIDTH))
        self.projectiles = pygame.sprite.Group()

    def launchProjectile(self):
        self.projectiles.add(Projectile(self))
        print("plouf")