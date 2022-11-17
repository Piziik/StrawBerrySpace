##Import all in settings file
import pygame.time

import settings
from settings import *
from Player import Player
from Enemy import Enemy

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
        self.player = Player(self.screen)
        self.enemies = pygame.sprite.Group()
        self.player.lastShot = 0
        self.timer = 3000
        self.monTimerEnregistre = pygame.time.get_ticks()

    ##Run method (keeps the game open)
    def run(self):
        ##The game loop
        while True:
            ##Method located in settings.py
            ScrollBackground(self)

            ##Display player, enemy & sprites
            self.player.update(settings)
            self.player.projectiles.update(self.enemies)
            self.enemies.update()

            if self.monTimerEnregistre + self.timer < pygame.time.get_ticks():
                self.monTimerEnregistre = pygame.time.get_ticks()
                self.enemies.add(Enemy(self.screen))
                self.timer = 500

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
                    settings.playerX = (self.screen.get_width() - PLAYER_HEIGHT)

            if pressed[pygame.K_SPACE] and self.player.isShooting is not True:
                self.player.launchProjectile()
                self.player.lastShot = pygame.time.get_ticks()

            if self.player.lastShot > 0 and pygame.time.get_ticks() - self.player.lastShot > 100:
                self.player.reload()

            if pressed[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()


            ##Update display
            pygame.display.update()