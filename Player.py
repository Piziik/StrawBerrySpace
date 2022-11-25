from settings import *
from Projectile import Projectile
from Game import *
import Game

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        ##Player image
        self.image = pygame.image.load('assets/entity/ship.png')
        self.image = pygame.transform.scale(self.image, (PLAYER_HEIGHT, PLAYER_WIDTH))
        self.rect = self.image.get_rect()
        ##Screen Surface
        self.screen = screen
        ##Player position
        self.rect.x = (SCREEN_WIDTH / 2) - (PLAYER_WIDTH / 2)
        self.rect.y = SCREEN_HEIGHT - 75
        ##Projectiles
        self.limProjectile = 1
        self.isShooting = False
        self.lastShot = 0
        ##All players projectiles
        self.projectiles = pygame.sprite.Group()

    ##Update player on screen
    def update(self, settings):
        # self.screen.blit(self.playerImage, (settings.playerX, settings.playerY))
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    ##Launch projectile
    def launchProjectile(self):
        if len(self.projectiles) < self.limProjectile and self.isShooting is not True:
            project = Projectile(self, self.screen)
            project.drawProjectile()
            self.projectiles.add(project)
            self.isShooting = True

    def reload(self):
        self.isShooting = False
        self.lastShot = 0
