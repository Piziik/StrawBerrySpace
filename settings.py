##Import pygame and sys library
import pygame
pygame.init()
import random
import sys


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