from settings import *
from Projectile import Projectile


class Player:
    def __init__(self, screen):
        ##Player image
        self.playerImage = pygame.image.load('assets/entity/ship.png')
        self.playerImage = pygame.transform.scale(self.playerImage, (PLAYER_HEIGHT, PLAYER_WIDTH))
        ##Screen Surface
        self.screen = screen
        ##Projectiles
        self.limProjectile = 3
        self.isShooting = False
        self.lastShot = 0
        ##All players projectiles
        self.projectiles = pygame.sprite.Group()

    ##Update player's projectiles
    def update(self, settings):
        self.screen.blit(self.playerImage, (settings.playerX, settings.playerY))

    ##Launch projectile
    def launchProjectile(self):
        if len(self.projectiles) < self.limProjectile and self.isShooting is not True:
            project = Projectile(self.screen)
            project.drawProjectile()
            self.projectiles.add(project)
            self.isShooting = True

    def reload(self):
        self.isShooting = False
        self.lastShot = 0
