import pygame as py
import sys
import utils
import button
import theme
from cases import Case
from pawn import Pawn

class Game():
    def __init__(self):
        # Create game Window
        py.init()

        self.screen = py.display.set_mode(
            (utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT))
        py.display.set_caption('Quorridor')
        self.clock = py.time.Clock()

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

        # Define font
        self.font = py.font.SysFont('arialbalck', 40)

        # Define colors
        self.TEXT_COLOR = (255, 255, 255)

        # Load button images # Should resize the pictures later
        help_img = py.image.load("assets\\help_button.png").convert_alpha()
        quit_img = py.image.load("assets\\quit_button.png").convert_alpha()
        start_img = py.image.load("assets\\start_button.png").convert_alpha()
        back_img = py.image.load("assets\\back_button.png").convert_alpha()

        # create button instances
        self.start_button = button.Button(
            utils.width_prct(40),
            utils.height_prct(25),
            start_img,
            1
        )

        self.help_button = button.Button(
            utils.width_prct(40),
            utils.height_prct(45),
            help_img, 
            1
            )
        
        self.quit_button = button.Button(
            utils.width_prct(40),
            utils.height_prct(65),
            quit_img, 
            1
            )
        
        self.back_button = button.Button(
            utils.width_prct(75),
            utils.height_prct(85),
            back_img, 
            1
            )
        

    # Show_methods
    def show_board(self, screen):
        self.screen.fill((119, 154, 88))
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



    # This is unused for now
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    # Event handler
    def check_events(self):
        for event in py.event.get():
            # Allows to quit the application correctly
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    print('test')

    # Game loop
    def mainloop(self):
        running = True

        while running:

            self.screen.fill((52, 78, 91))
            self.check_events()
    
            if self.game_state == "menu":

                # draw buttons
                # Simply means that the button has been clicked, returns a boolean
                
                # Buttons are clicked two by two, why? Try to change the coords in the blit method. It worked, buttons were too close to each other. I think it is due to the actual size of the pictures themselves
                if self.start_button.draw(self.screen):
                    # self.game_state = 'settings'
                    self.game_state = 'game'
                if self.help_button.draw(self.screen): self.game_state = 'help' # Simply means that the button has been clicked, returns a boolean




                if self.quit_button.draw(self.screen):  # Simply means that the button has been clicked, returns a boolean
                    py.quit()
                    sys.exit()


            elif self.game_state == 'help':
                self.draw_text(
                        """Each player in turn, chooses to move his pawn or to put up one of his fences. \nWhen he has run out of fences, the player must move his pawn.\n
                        At the beginning the board is empty.\n Choose and place your pawn in the center of the first line of your side of the board, your opponent takes another pawn and places it in the center of the first line of his side of the board(the one facing yours). Then take 10 fences each""",
                        self.font, 
                        self.TEXT_COLOR, 
                        utils.width_prct(5), 
                        utils.height_prct(5)
                        )
                if self.back_button.draw(self.screen): self.game_state = 'menu'
                
            elif self.game_state == 'game':
                self.show_board(self.screen)
                self.show_pawns()


            self.clock.tick(60)
            py.display.update()
            


if __name__ == "__main__":
    test = Game()
    test.mainloop()
