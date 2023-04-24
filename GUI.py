# Pygame and other modules
import pygame as py
import sys
import pygame_widgets
from pygame_widgets.dropdown import Dropdown


# Project files
import utils
import menu_button as button
import theme
from cases import Case
from pawn import Pawn



class Game():
    def __init__(self):
        # Create game Window
        py.init() # It is imperative to put this in the code, because it initializes all pygame modules
        self.screen = py.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT)) # Set the screen dimensions
        py.display.set_caption('Quorridor') # sets the screen title
        self.clock = py.time.Clock()



        self.board_size = Dropdown(
            self.screen,
            utils.width_prct(35),
            utils.height_prct(25),
            width=250,
            height=25,
            name='Selects the board size',
            choices=['5x5', '7x7', '9x9', '11x11'],
            borderRadius=3,
            colour=py.Color('beige'),
            values=[5, 7, 9, 11],
            direction='down',
            # eventType=py.MOUSEBUTTONDOWN
        )
        utils.ROWS = self.board_size.getSelected()

        self.number_of_players = Dropdown(
            self.screen,
            utils.width_prct(35),
            utils.height_prct(45),
            width=250,
            height=25,
            name='Selects the number of players',
            choices=['2', '3', '4'],
            borderRadius=3,
            colour=py.Color('beige'),
            values=[2, 3, 4],
            direction='down',
        )

        self.number_of_walls = Dropdown(
            self.screen,
            utils.width_prct(35),
            utils.height_prct(65),
            width=250,
            height=25,
            name='Selects the number of players',
            choices=['4', '20', '40'],
            borderRadius=3,
            colour=py.Color('beige'),
            values=[4, 20, 40],
            direction='down',
        )

        # pygame_widgets.update(py.event.poll())
        # py.event.clear()


        # This is my console board
        self.cases = [[0] * utils.COLS for i in range(utils.COLS)]
        # Turn squares into instances of another class(will serve to add some properties)
        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                self.cases[row][col] = Case(row, col) # Will give to each square the properties of the Case class


        # Game variables
        # self.game_paused = False
        self.game_state = 'menu'

        # Pawns
        self.red_pawn = Pawn('red')
        self.white_pawn = Pawn('white')

        # Load the pawn images
        self.red_pice = self.red_pawn.piece.convert_alpha()
        self.white_pice = self.white_pawn.piece.convert_alpha()


        # Load button images 
        help_img = py.image.load("assets\\help_button.png").convert_alpha()
        quit_img = py.image.load("assets\\quit_button.png").convert_alpha()
        start_img = py.image.load("assets\\start_button.png").convert_alpha()
        back_img = py.image.load("assets\\back_button.png").convert_alpha()
        resume_img = py.image.load("assets\\resume_button.png").convert_alpha()

        # create button instances
        self.start_button = button.Button(
            utils.width_prct(40), # x position
            utils.height_prct(25), # y position
            start_img, # The image
        )

        self.help_button = button.Button(
            utils.width_prct(40),
            utils.height_prct(45),
            help_img, # The image
            )
        
        self.quit_button = button.Button(
            utils.width_prct(40),
            utils.height_prct(65),
            quit_img, 
            )
        
        self.back_button = button.Button(
            utils.width_prct(60), # x coordinate
            utils.height_prct(85), # y coordinate
            back_img, 
            )
        
        self.resume_button = button.Button(
            utils.width_prct(25),
            utils.height_prct(85),
            resume_img, 
            )
        

    # Show_methods
    def show_board(self, screen):
        self.screen.fill((119, 154, 88)) # Board color
        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                rect = (col * utils.SQSIZE, row * utils.SQSIZE, utils.SQSIZE, utils.SQSIZE) # rectangle dimensions
                py.draw.rect(screen, theme.board_color, rect, 1)

    def show_pawns(self):

        # Display pawns

        # Red pawn
        self.cases[utils.ROWS // 2][-1] = Case(utils.ROWS // 2, -1, self.red_pawn) # The format is [row][col]
        # White pawn
        self.cases[utils.ROWS // 2][0] = Case(utils.ROWS // 2, 0, self.white_pawn)

        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                piece_rect = col * utils.SQSIZE + utils.SQSIZE // 2, row * utils.SQSIZE + utils.SQSIZE // 2 # Put the piece at the center of the square
                if self.cases[row][col].has_pawn(): # Check if the square has a pawn
                    if self.cases[row][col] == self.cases[utils.ROWS // 2][-1]:
                        
                        self.screen.blit(
                            self.red_pawn.piece, 
                            self.red_pawn.piece.get_rect(center=piece_rect)
                            )
                    elif self.cases[row][col] == self.cases[utils.ROWS // 2][0]:
                        self.screen.blit(
                            self.white_pawn.piece,
                            self.white_pawn.piece.get_rect(center=piece_rect)
                        )


    # Event handler
    def check_events(self):
        pass
        # for event in py.event.get():
        #     # Allows to quit the application correctly
        #     if event.type == py.QUIT:
        #         py.quit()
        #         sys.exit()
        #     elif event.type  == py.MOUSEBUTTONDOWN or event.type == py.MOUSEBUTTONUP: 
        #         pass
        #     # This is a test
        #     elif event.type == py.KEYDOWN or event.type == py.KEYUP:
        #         if event.key == py.K_SPACE:
        #             print('test')
            # else:
            #     self.mainloop(event)


    # Game loop
    def mainloop(self):

        while True:

            self.screen.fill((250, 52, 25)) # Background color
            # self.check_events()

            for event in py.event.get():
                # Allows to quit the application correctly
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()
                elif event.type  == py.MOUSEBUTTONDOWN or event.type == py.MOUSEBUTTONUP: 
                    pass
                # This is a test
                elif event.type == py.KEYDOWN or event.type == py.KEYUP:
                    if event.key == py.K_SPACE:
                        print('test')
            
            if self.game_state == "menu": # If the game is in the menu stat, it will display the menu
                
                if self.start_button.display(self.screen):
                    # self.game_state = 'settings'
                    self.game_state = 'utils' # the start game must redirect the user to the 'utils' page which will then bring him to the game
                if self.help_button.display(self.screen): self.game_state = 'help' # Simply means that the button has been clicked, returns a boolean


                if self.quit_button.display(self.screen):  # Simply means that the button has been clicked, returns a boolean
                    py.quit()
                    sys.exit()


            elif self.game_state == 'help': # else if the game is in the 'help' state, it will display the help menu
                # Display the rules
                if self.back_button.display(self.screen): self.game_state = 'menu'
                
            elif self.game_state == 'game': # else if the game is in the 'game' state, it will launch the game
                self.show_board(self.screen)
                self.show_pawns()

            elif self.game_state == 'utils': 
                pygame_widgets.update(py.event.poll())
                # utils.ROWS = self.board_size.getSelected()
                # print(utils.ROWS)
                if self.back_button.display(self.screen): self.game_state = 'menu'
                if self.resume_button.display(self.screen): self.game_state = 'game'





            self.clock.tick(60)
            
            py.display.update()
            


if __name__ == "__main__":
    test = Game()
    test.mainloop()
