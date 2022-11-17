import settings
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        ##Projectile image
        self.projectileImage = pygame.image.load('assets/entity/projectile.png')
        self.projectileImage = pygame.transform.scale(self.projectileImage, (PROJECTILE_HEIGHT, PROJECTILE_WIDTH))
        self.rect = self.projectileImage.get_rect()
        ##Projectile coord
        self.rect.x = settings.playerX
        self.rect.y = settings.playerY - PLAYER_HEIGHT
        ##Screen Surface
        self.screen = screen

    ##Diplay projectiles sprite
    def drawProjectile(self):
        self.screen.blit(self.projectileImage, (self.rect.x, self.rect.y))

    ##Kill projectile if it's not in the screen
    def update(self):
        self.rect.y -= projectileVelocity
        self.screen.blit(self.projectileImage, (self.rect.x, self.rect.y))
        if self.rect.y <= 0:
            self.kill()