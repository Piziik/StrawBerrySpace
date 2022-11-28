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

        ##Menu background
        self.menuBackgound = pygame.image.load('assets/img/background-black.png')
        ##Rescale background
        self.menuBackgound = pygame.transform.scale(self.menuBackgound, (SCREEN_WIDTH, SCREEN_HEIGHT))

        white = (255, 255, 255)

        ##Create a font object for the Title
        self.fontTitle = pygame.font.Font('assets/font/SpaceMission.otf', 64)
        ##Create a text
        self.title = self.fontTitle.render('StrawBerry Space', True, white, None)
        self.titleRect = self.title.get_rect()
        self.titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 700)

        self.fontTxt = pygame.font.Font('assets/font/8-BIT WONDER.TTF', 40)
        self.textStart = self.fontTxt.render('START', True, white, None)
        self.textStartReact = self.textStart.get_rect()
        self.textStartReact.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.fontTxt = pygame.font.Font('assets/font/8-BIT WONDER.TTF', 18)
        self.textCredit = self.fontTxt.render('CREDITS', True, white, None)
        self.textCreditReact = self.textCredit.get_rect()
        self.textCreditReact.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 50)

        self.textQuit = self.fontTxt.render('EXIT', True, white, None)
        self.textQuitReact = self.textQuit.get_rect()
        self.textQuitReact.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT //2) + 100)

    ##Run method (keeps the menu open)
    def run(self):
        ##The menu loop
        while True:
            self.screen.blit(self.menuBackgound, (0, 0))
            self.screen.blit(self.title, self.titleRect)
            self.screen.blit(self.textStart, self.textStartReact)
            self.screen.blit(self.textCredit, self.textCreditReact)
            self.screen.blit(self.textQuit, self.textQuitReact)
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