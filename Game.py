##Import all in settings file
import pygame.time
import settings
from settings import *
from Player import Player
from Enemy import Enemy
from DeathScreen import *

##Game class
class Game:
    ##Constructor
    def __init__(self):
        ##Init pygame library
        pygame.init()

        ##Screen size
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800

        ##Change the window's icon
        self.icon = pygame.image.load('assets/img/strawberry.png')
        pygame.display.set_icon(self.icon)

        ##Game background
        self.gameBackgound = pygame.image.load('assets/img/background-black.png')
        ##Rescale background
        self.gameBackgound = pygame.transform.scale(self.gameBackgound, (SCREEN_WIDTH, SCREEN_HEIGHT))

        ##Create a window for the game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        ##Change the window's caption
        pygame.display.set_caption('StrawBerrySpace - Adventure')
        self.player = Player(self.screen)
        self.enemies = pygame.sprite.Group()
        self.player.lastShot = 0
        self.timer = 2000
        self.monTimerEnregistre = pygame.time.get_ticks()

        white = (255, 255, 255)
        self.fontTxt = pygame.font.Font('assets/font/SpaceMission.otf', 24)


    ##Method ScrollBackground() (allows the program to scroll the background, so it gives the impression that the character is moving forward)
    def ScrollBackground(self):
        global position
        ##Fill the surface w/ a solid color
        self.screen.fill((0, 0, 0))
        ##Display a fist background image at x = 0, y = 0
        self.screen.blit(self.gameBackgound, (0, 0 + position))
        ##Display a second background image at x = 0, y = -600 + position
        self.screen.blit(self.gameBackgound, (0, - self.gameBackgound.get_height() + position))
        ##Decrease or increase the scroll speed
        position += 3
        ##When the first image disappear, the image is relocated behind the other image to reaper after and so on
        if abs(position) > self.gameBackgound.get_height():
            position = 0
    ##Run method (keeps the game open)
    def run(self):
        ##The game loop
        while True:
            ##Method located in settings.py
            Game.ScrollBackground(self)

            ##Display player, enemy & sprites
            self.player.update(settings)
            self.player.projectiles.update(self.enemies)
            self.enemies.update()

            ##KillCountDisplay
            self.textKills = self.fontTxt.render(f'Kills {self.player.killCount}', True, (255, 255, 255), None)
            self.textKillsReact = self.textKills.get_rect()
            self.textKillsReact.center = (60, 20)
            self.screen.blit(self.textKills, self.textKillsReact)

            if self.monTimerEnregistre + self.timer < pygame.time.get_ticks():
                self.monTimerEnregistre = pygame.time.get_ticks()
                self.enemies.add(Enemy(self.screen))
                self.timer = 1000

            pressed = pygame.key.get_pressed()
            ##Collision Player-Enemy
            if pygame.sprite.spritecollide(self.player, self.enemies, False, pygame.sprite.collide_mask):
                deathScreen = DeathScreen()
                deathScreen.run()
            ##Quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            ##Move player
            if pressed[pygame.K_LEFT]:
                self.player.rect.x -= settings.playerVelocity
                if self.player.rect.x <= 0:
                    self.player.rect.x = 0
            if pressed[pygame.K_RIGHT]:
                self.player.rect.x += settings.playerVelocity
                if self.player.rect.x >= (self.screen.get_width() - PLAYER_HEIGHT):
                    self.player.rect.x = (self.screen.get_width() - PLAYER_HEIGHT)
            ##Player shoot
            if pressed[pygame.K_SPACE] and self.player.isShooting is not True:
                self.player.launchProjectile()
                self.player.lastShot = pygame.time.get_ticks()

            if self.player.lastShot > 0 and pygame.time.get_ticks() - self.player.lastShot > 200:
                self.player.reload()
            ##Quitte le jeu
            if pressed[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            ##Update display
            pygame.display.update()