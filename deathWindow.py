##Impport
from settings import *

##Menu Class
class deathWindow:
    ##Constructor
    def __init__(self):
        ##Init pygame library
        pygame.init()
        ##Create a window for the game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        ##Change the window's caption
        pygame.display.set_caption('StrawBerrySpace - Death')

    ##Run method (keeps the menu open)
    def run(self):
        ##The menu loop
        while True:
            self.screen.blit(menuBackgound, (0, 0))
            self.screen.blit(title, titleRect)
            self.screen.blit(textEnd, textStartReact)
            self.screen.blit(textQuit, textQuitReact)
            ##Quit the Menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            ##Update display
            pygame.display.update()