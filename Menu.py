##Impport
from settings import *
from Game import Game

##Menu Class
class Menu:
    ##Constructor
    def __init__(self):
        ##Init pygame library
        pygame.init()
        ##Create a window for the game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        ##Change the window's caption
        pygame.display.set_caption('StrawBerrySpace - Menu')

    ##Run method (keeps the menu open)
    def run(self):
        ##The menu loop
        while True:
            self.screen.blit(menuBackgound, (0, 0))
            self.screen.blit(title, titleRect)
            self.screen.blit(textStart, textStartReact)
            self.screen.blit(textQuit, textQuitReact)
            ##Quit the Menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Launch the game if "RETURN" key is pressed
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_RETURN]:
                    game = Game()
                    game.run()
                if pressed[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            ##Update display
            pygame.display.update()