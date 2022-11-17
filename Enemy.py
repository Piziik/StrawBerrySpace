import settings
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        ##Enemy image
        self.enemyImage = pygame.image.load('assets/entity/strawberry.png')
        self.enemyImage = pygame.transform.scale(self.enemyImage, (ENEMY_HEIGHT, ENEMY_WIDTH))
        self.rect = self.enemyImage.get_rect()
        ##Enemy coord
        self.rect.x = settings.enemyX
        self.rect.y = settings.enemyY - ENEMY_HEIGHT
        ##Screen Surface
        self.screen = screen

    ##Update enemy on screen
    def drawEnemies(self, settings):
        self.screen.blit(self.enemyImage, (settings.enemyX, settings.enemyY))

    ##Kill enemy if it's not in the screen
    def update(self):
        self.rect.y += enemyVelocity
        self.screen.blit(self.enemyImage, (self.rect.x, self.rect.y))