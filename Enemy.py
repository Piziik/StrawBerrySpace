import settings
from settings import *
from DeathScreen import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        ##Enemy image
        self.image = pygame.image.load('assets/entity/strawberry.png')
        self.image = pygame.transform.scale(self.image, (ENEMY_HEIGHT, ENEMY_WIDTH))
        self.rect = self.image.get_rect()
        ##Enemy coord
        self.rect.x = random.randint(0, 755)
        self.rect.y = 0 - ENEMY_HEIGHT
        ##Screen Surface
        self.screen = screen

    ##Display enemy on screen
    def drawEnemies(self, settings):
        self.screen.blit(self.image, (settings.enemyX, settings.enemyY))

    ##Kill enemy if it's not in the screen
    def update(self):
        self.rect.y += enemyVelocity
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.y == settings.SCREEN_HEIGHT:
            deathScreen = DeathScreen()
            deathScreen.run()
