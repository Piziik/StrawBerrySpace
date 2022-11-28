import settings
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, screen):
        super().__init__()
        ##Projectile image
        self.projectileImage = pygame.image.load('assets/entity/projectile.png')
        self.projectileImage = pygame.transform.scale(self.projectileImage, (PROJECTILE_HEIGHT, PROJECTILE_WIDTH))
        self.rect = self.projectileImage.get_rect()
        ##Projectile coord
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y - PLAYER_HEIGHT
        ##Screen Surface
        self.screen = screen
        self.player = player

    ##Diplay projectiles sprite
    def drawProjectile(self):
        self.screen.blit(self.projectileImage, (self.rect.x, self.rect.y))

    ##Kill projectile if it's not in the screen
    def update(self, enemies):
        self.rect.y -= projectileVelocity
        self.screen.blit(self.projectileImage, (self.rect.x, self.rect.y))
        for enemy in enemies:
            if enemy.rect.x - ENEMY_WIDTH / 2 <= self.rect.x <= enemy.rect.x + ENEMY_WIDTH / 2 and enemy.rect.y > self.rect.y - PROJECTILE_HEIGHT:
                self.player.killCount += 1
                print(self.player.killCount)
                enemy.kill()
                self.kill()

        if self.rect.y <= 0:
            self.kill()

