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
from dragger import Dragger



class Game():
    def __init__(self):

        # Create game Window
        py.init() # It is imperative to put this in the code, because it initializes all pygame modules
        self.screen = py.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT)) # Set the screen dimensions
        py.display.set_caption('Quorridor') # sets the screen title
        self.clock = py.time.Clock()
        self.dragger = Dragger()

        # This is my console board
        self.cases = [[0] * utils.COLS for i in range(utils.COLS)]
        # Turn squares into instances of another class(will serve to add some properties)
        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                self.cases[row][col] = Case(row, col) # Will give to each square the properties of the Case class

        # Game state variables
        # self.game_paused = False
        self.game_state = 'menu'

        # Pawns
        self.red_pawn = Pawn('red')
        self.white_pawn = Pawn('white')

        # Load the pawn images
        self.red_pice = self.red_pawn.piece.convert_alpha()
        self.white_pice = self.white_pawn.piece.convert_alpha()
        rect_test = self.red_pice.get_rect()
        pos = py.mouse.get_pos()
        if rect_test.collidepoint(pos):
            print('Yes yes yes!!')

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
        screen.fill((119, 154, 88)) # Board color
        for row in range(utils.ROWS):
            for col in range(utils.COLS):

                # Squares
                squares_rect = (col * utils.SQSIZE, row * utils.SQSIZE, utils.SQSIZE, utils.SQSIZE) # rectangle dimensions, the format is (row, col, width, height)
                self.squares = py.draw.rect(screen, theme.board_color, squares_rect, 1) # Is the "self" really necessary?

    def show_walls(self, screen):
        # test colors
        RED = (255, 0, 0)
        blc = (0, 0, 0)

        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                # Horizontal wall spots
                horiz_rect = (col * utils.SQSIZE, (row+1) * utils.SQSIZE, utils.SQSIZE, 10)
                horizontal_walls = py.draw.rect(screen, RED, horiz_rect, 1)
        
                # Vertical walls
                vert_rect = ((col+1) * utils.SQSIZE, row * utils.SQSIZE, 10, utils.SQSIZE)
                vert_walls = py.draw.rect(screen, RED, vert_rect)

                # Click handler
                pos = py.mouse.get_pos()
                if horizontal_walls.collidepoint(pos):
                    if py.mouse.get_pressed()[0] == 1 and not self.dragger.dragging: # and self.clicked == False:
                        # self.clicked = True
                        horizontal_walls = py.draw.rect(screen, blc, horiz_rect, 1)
                        print('tesr')

                if vert_walls.collidepoint(pos):
                    # and self.clicked == False:
                    if py.mouse.get_pressed()[0] == 1:
                    # self.clicked = True
                        vert_walls = py.draw.rect(screen, blc, vert_rect, 1)
                        print('tesr')
                
    def show_pawns(self, screen):

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
                        screen.blit(
                            self.red_pawn.piece, 
                            self.red_pawn.piece.get_rect(center=piece_rect) # You can sort  this in a rect variable to use later with collidepoint
                            )
                        
                    elif self.cases[row][col] == self.cases[utils.ROWS // 2][0]:
                        screen.blit(
                            self.white_pawn.piece,
                            self.white_pawn.piece.get_rect(center=piece_rect)
                        )

    # Event handler
    def check_events(self):
        # pass
        for event in py.event.get():
            # Allows to quit the application correctly
            if event.type == py.QUIT:
                py.quit()
                sys.exit()




    # Game loop
    def mainloop(self):
        board_sizes = Dropdown(
            self.screen, 
            200, #x
            200, #y
            100, #width
            50, #height
            "This is a test",
            ["5x5", "7x7", "9x9", "11x11"],
            eventType = py.MOUSEBUTTONDOWN
            )
        # number_of_players = Dropdown(self.screen, 200, 300, 100, 50, [2, 3, 4])
        # number_of_walls = Dropdown(self.screen, 200, 400, 100, 50, [20, 40, 80])
        selected_board_size = 5
        selected_number_of_players = 2
        selected_number_of_walls = 20

        while True:
            self.screen.fill((250, 52, 25))  # Background color
            self.check_events()

            if self.game_state == "menu":
                if self.start_button.display(self.screen):
                    self.game_state = 'utils'
                if self.help_button.display(self.screen):
                    self.game_state = 'help'
                if self.quit_button.display(self.screen):
                    py.quit()
                    sys.exit()

            elif self.game_state == 'help':
                if self.back_button.display(self.screen):
                    self.game_state = 'menu'

            elif self.game_state == 'game':
                self.show_board(self.screen)
                self.show_walls(self.screen)
                self.show_pawns(self.screen)

                if self.dragger.dragging:
                    self.dragger.update_screen(self.screen)

                for event in py.event.get():
                    if event.type == py.MOUSEBUTTONDOWN:
                        self.dragger.update_mouse(event.pos)
                        clicked_row = self.dragger.pos_y // utils.SQSIZE
                        clicked_col = self.dragger.pos_x // utils.SQSIZE

                        if self.cases[clicked_row][clicked_col].has_pawn():
                            print('The click works')
                            pawn = self.cases[clicked_row][clicked_col].pawn
                            self.dragger.save_initial(event.pos)
                            self.dragger.drag_pawn(pawn)

                    if event.type == py.MOUSEMOTION:
                        # If we are dragging the pawn
                        if self.dragger.dragging:
                            self.dragger.update_mouse(event.pos)
                            self.dragger.update_screen(self.screen)

                    if event.type == py.MOUSEBUTTONUP:
                        self.dragger.undrag_pawn()
                
            elif self.game_state == 'utils':
                if self.back_button.display(self.screen):
                    self.game_state = 'menu'

                if self.resume_button.display(self.screen):
                    self.game_state = 'game'

                # Below is a useless code
                selected_board_size = board_sizes.getSelected()
                # selected_number_of_players = int(number_of_players.getValue())
                # selected_number_of_walls = int(number_of_walls.getValue())

                # board_sizes.listen()
                # number_of_players.listen()
                # number_of_walls.listen()

                board_sizes.draw()
                # number_of_players.draw()
                # number_of_walls.draw()

            self.clock.tick(60)
            py.display.update()



if __name__ == "__main__":
    game = Game()
    game.mainloop()