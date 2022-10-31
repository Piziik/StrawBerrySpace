##Import Game Class
from Game import *
##Import Menu Class
from Menu import *

# def startTheGame():
#     ##Check if we are in the right file
#     if __name__ == '__main__':
#         ##Then launch the game
#         game = Game()
#         game.run()

def mainMenu():
    ##Check if we are in the right file
    if __name__ == '__main__':
        ##Then launch the game
        menu = Menu()
        menu.run()


##Launch Menu
mainMenu()

##Launch Game
# startTheGame()