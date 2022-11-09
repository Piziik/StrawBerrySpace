import settings
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.projectileImage = pygame.image.load('assets/entity/projectile.png')
        self.projectileImage = pygame.transform.scale(self.projectileImage, (PROJECTILE_HEIGHT, PROJECTILE_WIDTH))
        self.rect = self.projectileImage.get_rect()
        self.rect.x = settings.playerX
        self.rect.y = settings.playerY