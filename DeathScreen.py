##Impport
from settings import *

##Menu Class
class DeathScreen:
    ##Constructor
    def __init__(self):
        ##Init pygame library
        pygame.init()
        ##Create a window for the game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        ##Change the window's caption
        pygame.display.set_caption('StrawBerrySpace - Death')

        ##Death screen background
        self.deathScreenBackgound = pygame.image.load('assets/img/background-black.png')
        ##Rescale background
        self.deathScreenBackgound = pygame.transform.scale(self.deathScreenBackgound, (SCREEN_WIDTH, SCREEN_HEIGHT))

        white = (255, 255, 255)

        ##Create a font object for the Title
        self.fontTitre = pygame.font.Font('assets/font/8-BIT WONDER.TTF', 32)
        self.fontTxt = pygame.font.Font('assets/font/8-BIT WONDER.TTF', 16)
        self.textEnd = self.fontTitre.render('Fin de la partie', True, white, None)
        self.textEndReact = self.textEnd.get_rect()
        self.textEndReact.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.textQuit = self.fontTxt.render('( Press ESCAPE to Quit )', True, white, None)
        self.textQuitReact = self.textQuit.get_rect()
        self.textQuitReact.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200)

    ##Run method (keeps the death screen open)
    def run(self):
        ##The menu loop
        while True:
            self.screen.blit(self.deathScreenBackgound, (0, 0))
            self.screen.blit(self.textEnd, self.textEndReact)
            self.screen.blit(self.textQuit, self.textQuitReact)
            ##Quit the Menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
            ##Update display
            pygame.display.update()