##Import pygame and sys library
import pygame
import random
import sys
pygame.init()

#<editor-fold desc="Game Window Settings">

##----GAME WINDOW SETTINGS----##

##Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

##Change the window's icon
icon = pygame.image.load('assets/img/strawberry.png')
pygame.display.set_icon(icon)

##Game background
gameBackgound = pygame.image.load('assets/img/background-black.png')
##Rescale background
gameBackgound = pygame.transform.scale(gameBackgound, (SCREEN_WIDTH, SCREEN_HEIGHT))

##Variable for the ScrollBackground() method
position = 0

##Method ScrollBackground() (allows the program to scroll the background, so it gives the impression that the character is moving forward)
def ScrollBackground(self):
    global position
    ##Fill the surface w/ a solid color
    self.screen.fill((0, 0, 0))
    ##Display a fist background image at x = 0, y = 0
    self.screen.blit(gameBackgound, (0, 0 + position))
    ##Display a second background image at x = 0, y = -600 + position
    self.screen.blit(gameBackgound, (0, - gameBackgound.get_height() + position))
    ##Decrease or increase the scroll speed
    position += 3
    ##When the first image disappear, the image is relocated behind the other image to reaper after and so on
    if abs(position) > gameBackgound.get_height():
        position = 0

#</editor-fold>

#<editor-fold desc="Menu Window Settings">

##----MENU WINDOW SETTINGS----##

##Menu background
menuBackgound = pygame.image.load('assets/img/background-black.png')
##Rescale background
menuBackgound = pygame.transform.scale(menuBackgound, (SCREEN_WIDTH, SCREEN_HEIGHT))

white = (255, 255, 255)

##Create a font object for the Title
fontTitle = pygame.font.Font('assets/font/SpaceMission.otf', 64)
##Create a text
title = fontTitle.render('StrawBerry Space', True, white, None)
titleRect = title.get_rect()
titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 700)

fontTxt = pygame.font.Font('assets/font/8-BIT WONDER.TTF', 16)
textStart = fontTxt.render('Press ENTER to start', True, white, None)
textStartReact = textStart.get_rect()
textStartReact.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

textQuit = fontTxt.render('( Press ESCAPE to Quit )', True, white, None)
textQuitReact = textQuit.get_rect()
textQuitReact.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200)

fontTxt = pygame.font.Font('assets/font/8-BIT WONDER.TTF', 16)
textEnd = fontTxt.render('Vous êtes mort', True, white, None)
textEndReact = textStart.get_rect()
textEndReact.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

##Create a font object for

#</editor-fold>

#<editor-fold desc="Player settings">#
PLAYER_HEIGHT = 45
PLAYER_WIDTH = 45
playerVelocity = 8
playerX = (SCREEN_WIDTH / 2) - (PLAYER_WIDTH / 2)
playerY = SCREEN_HEIGHT - 75
#</editor-fold>#

#<editor-fold desc="Projectile settings">#
PROJECTILE_HEIGHT = 50
PROJECTILE_WIDTH = 50
projectileVelocity = 20
projectileX = (SCREEN_WIDTH / 2) - (PLAYER_WIDTH / 2)
projectileY = SCREEN_HEIGHT - 75
#</editor-fold>#

#<editor-fold desc="Enemy settings">#
ENEMY_HEIGHT = 60
ENEMY_WIDTH = 60
enemyVelocity = 2
#</editor-fold>#