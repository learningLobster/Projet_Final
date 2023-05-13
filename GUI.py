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
from move import Move


class Game():
    def __init__(self):

        # Create game Window
        py.init()  # It is imperative to put this in the code, because it initializes all pygame modules
        self.screen = py.display.set_mode(
            (utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT))  # Set the screen dimensions
        py.display.set_caption('Quorridor')  # sets the screen title
        self.clock = py.time.Clock()
        self.dragger = Dragger()

        # This is my console board
        self.cases = [[0] * utils.COLS for i in range(utils.COLS)]
        # Turn squares into instances of another class(will serve to add some properties)
        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                # Will give to each square the properties of the Case class
                self.cases[row][col] = Case(row, col)

        # Game state variables
        # self.game_paused = False
        self.game_state = 'menu'

        # Move related variables
        self.last_move = None  # I don't think I'll need but it can be useful
        # self.player = "white"
        self.player = "white"

        # Pawns
        self.red_pawn = Pawn('red')
        self.white_pawn = Pawn('white')
        self.black_pawn = Pawn('black')
        self.green_pawn = Pawn('green')

        # Load the pawn images
        self.red_piece = self.red_pawn.img.convert_alpha()
        self.white_piece = self.white_pawn.img.convert_alpha()
        self.black_piece = self.black_pawn.img.convert_alpha()
        self.green_piece = self.green_pawn.img.convert_alpha()

        # Position the pawns in the console board
        self.set_pawn_position(utils.ROWS//2, 0, "red")
        self.set_pawn_position(utils.ROWS//2, -1, "white")
        self.set_pawn_position(0, utils.ROWS//2, "black")
        self.set_pawn_position(-1, utils.ROWS//2, "green")

        # Load button images
        help_img = py.image.load("assets\\help_button.png").convert_alpha()
        quit_img = py.image.load("assets\\quit_button.png").convert_alpha()
        start_img = py.image.load("assets\\start_button.png").convert_alpha()
        back_img = py.image.load("assets\\back_button.png").convert_alpha()
        resume_img = py.image.load("assets\\resume_button.png").convert_alpha()

        # create button instances
        self.start_button = button.Button(
            utils.width_prct(40),  # x position
            utils.height_prct(25),  # y position
            start_img,  # The image
        )

        self.help_button = button.Button(
            utils.width_prct(40),
            utils.height_prct(45),
            help_img,  # The image
        )

        self.quit_button = button.Button(
            utils.width_prct(40),
            utils.height_prct(65),
            quit_img,
        )

        self.back_button = button.Button(
            utils.width_prct(60),  # x coordinate
            utils.height_prct(85),  # y coordinate
            back_img,
        )

        self.resume_button = button.Button(
            utils.width_prct(25),
            utils.height_prct(85),
            resume_img,
        )


    # Show_methods
    def show_board(self, screen):
        screen.fill(theme.board_color)  # Board color (119, 154, 88)
        for row in range(utils.ROWS):
            for col in range(utils.COLS):

                # Squares
                # rectangle dimensions, the format is (row, col, width, height)
                squares_rect = (col * utils.SQSIZE, row *
                                utils.SQSIZE, utils.SQSIZE, utils.SQSIZE)
                # Is the "self" really necessary?
                self.squares = py.draw.rect(
                    screen, theme.board_color, squares_rect, 1) # Lines colors
                # self.squares got collidepoint as well


    def show_walls(self, screen):
        # test colors
        RED = (255, 0, 0)
        blc = (0, 0, 0)

        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                # Horizontal wall spots
                horiz_rect = (
                    col * utils.SQSIZE, 
                    (row+1) * utils.SQSIZE, 
                    utils.SQSIZE, 
                    10
                    )
                horizontal_walls = py.draw.rect(screen, RED, horiz_rect, 1)

                # Vertical walls
                vert_rect = (
                    (col+1) * utils.SQSIZE, 
                    row * utils.SQSIZE, 
                    10, 
                    utils.SQSIZE
                    )
                vert_walls = py.draw.rect(screen, RED, vert_rect)

                # Click handler
                pos = py.mouse.get_pos()
                if horizontal_walls.collidepoint(pos):
                    # and self.clicked == False:
                    if py.mouse.get_pressed()[0] == 1 and not self.dragger.dragging:
                        # self.clicked = True
                        horizontal_walls = py.draw.rect(
                            screen, blc, horiz_rect, 1)

                if vert_walls.collidepoint(pos):
                    # and self.clicked == False:
                    if py.mouse.get_pressed()[0] == 1:
                        # self.clicked = True
                        vert_walls = py.draw.rect(screen, blc, vert_rect, 1)


    # Set the postion of each pawn in the console board
    def set_pawn_position(self, row, col, color):
        if color == "white":
            self.cases[row][col] = Case(row, col, self.white_pawn)
        elif color == "red":
            self.cases[row][col] = Case(row, col, self.red_pawn)
        elif color == "black":
            self.cases[row][col] = Case(row, col, self.black_pawn)
        elif color == "green": # Or you can use an else statement
            self.cases[row][col] = Case(row, col, self.green_pawn)
        return self.cases[row][col]
    

    # Display pawns
    def show_pawns(self, screen):

        for row in range(utils.ROWS):
            for col in range(utils.COLS):
                # I position the pawns in this loop
                
                if self.cases[row][col].has_pawn():  # Check if the square has a pawn
                    pawn = self.cases[row][col].pawn

                    if pawn is not self.dragger.pawn:
                        # Draws(blits) the pawns and nothing else
                        img_rect = col * utils.SQSIZE + utils.SQSIZE // 2, \
                            row * utils.SQSIZE + utils.SQSIZE // 2  # Put the piece at the center of the square

                        if pawn.color == 'white':
                            white_img = self.white_pawn.img
                            white_rect = white_img.get_rect(center=img_rect)
                            screen.blit(
                                white_img,  # This is the image
                                white_rect
                            )

                        elif pawn.color == 'red':
                            red_img = self.red_pawn.img
                            red_rect = red_img.get_rect(center=img_rect)
                            screen.blit(
                                red_img,  # This is the image
                                red_rect
                            )

                        elif pawn.color == 'black':
                            black_img = self.black_pawn.img
                            black_rect = black_img.get_rect(center=img_rect)
                            screen.blit(
                                black_img,  # This is the image
                                black_rect
                            )
                            
                        elif pawn.color == 'green': # You can use an else
                            green_img = self.green_pawn.img
                            green_rect = green_img.get_rect(center=img_rect)
                            screen.blit(
                                green_img,  # This is the image
                                green_rect
                            )
                        
                        print(
                            f"{pawn.color}'s row: {self.cases[row][col].row}")
                        print(f"{pawn.color}'s col: {self.cases[row][col].col}")
                        # print(f"{self.white_pawn.color}'s row: {self.white_pawn.row}")
                        # print(f"{self.white_pawn.color}'s col: {self.white_pawn.col}")
                        # print(f"{self.black_pawn.color}'s row: {self.black_pawn.row}")
                        # print(f"{self.black_pawn.color}'s col: {self.black_pawn.col}")
                        # print(f"{self.green_pawn.color}'s row: {self.green_pawn.row}")
                        # print(f"{self.green_pawn.color}'s col: {self.green_pawn.col}")


    def show_moves(self, screen):
        if self.dragger.dragging:
            pawn = self.dragger.pawn

            # Loop all valid moves
            for move in pawn.moves:
                # color
                color = 'cyan'  # You should definitely change this color
                # color = 'blue' if (move.final.row+move.final.col) % 2 == 0 else 'lightblue'
                # rect
                rect = (move.final.col * utils.SQSIZE, move.final.row *
                        utils.SQSIZE, utils.SQSIZE, utils.SQSIZE)
                # blit
                py.draw.rect(screen, color, rect)


    def calc_moves(self, pawn, row, col): # Calc move works perfectly, at least it returns the right squares. It does return the right result
        number = 0 # Don't think I really need this anymore, It was used to debug the chess problem
        """
            Calculates the possible moves
        """
        # if isinstance(piece, Pawn):
        # A set of all possible movements
        possible_moves = [
            (row, col-1),  # left
            (row, col+1),  # right
            (row-1, col),  # up
            (row+1, col)  # down
        ]
        for possible_move in possible_moves:
            possible_move_row, possible_move_col = possible_move

            if Case.in_range(possible_move_row, possible_move_col): # If the moves are in range of the board(if they don't exceed the board size)
                if self.cases[possible_move_row][possible_move_col].empty():
                    if not self.cases[possible_move_row][possible_move_col].has_pawn():
                    
                        # A debug, I think?
                        if self.cases[possible_move_row][possible_move_col].pawn != None:
                            print(number)

                
                        # Creates new cases
                        initial = Case(row, col)
                        final = Case(possible_move_row, possible_move_col)

                        # Create new move
                        move = Move(initial, final)
                        pawn.add_move(move)

                        number += 1
                    
                else: #self.cases[possible_move_row][possible_move_col].has_pawn(): # I can either use this condition to make the code perfect or I can just make a turn function and that should do the trick
                    enemy_pos = self.cases[possible_move_row][possible_move_col]

                    # It is 00:46 on the 11/05/2023, you are tired and your nested condition are getting messy. You should definitely check them and prevent them from jumping two squares
                    if enemy_pos.row == row:
                        possible_moves.append((enemy_pos.row, enemy_pos.col+1))

                    elif enemy_pos.col == col:
                        possible_moves.append((enemy_pos.row+1, enemy_pos.col))
                    
                    elif (enemy_pos.row == row) and (enemy_pos.col == col):  # Don't know if I could use an else instead
                        possible_moves.append((enemy_pos.row+1, enemy_pos.col))
                        possible_moves.append((enemy_pos.row, enemy_pos.col+1))
                # elif self.cases[possible_move_row][possible_move_col].has_pawn():
                    

    def move_pawn(self, pawn, move):

        initial = move.initial
        final = move.final

        self.cases[initial.row][initial.col].pawn = None
        self.cases[final.row][final.col].pawn = pawn

        # Move
        # pawn.moved = True # Is it really important? Not really

        # Clear valid moves
        pawn.clear_moves()

        # Sets last move
        # self.last_move = move


    # Check if a move is valid and prevents invalid ones
    def valid_move(self, pawn, move):
        if pawn != None:
            return move in pawn.moves
    

    # Event handler
    def check_events(self):

        for event in py.event.get():
            # Allows to quit the application correctly
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.MOUSEBUTTONDOWN:
                self.dragger.update_mouse(event.pos) # update the mouse position
                clicked_row = self.dragger.pos_y // utils.SQSIZE # Returns the row that was clicked
                clicked_col = self.dragger.pos_x // utils.SQSIZE # Returns the column that was clicked

                if self.cases[clicked_row][clicked_col].has_pawn(): # Checks wether the clicked cell has a pawn
                    pawn = self.cases[clicked_row][clicked_col].pawn # Stores the pawn from the clicked cell into the pawn variable

                    if pawn.color == self.player:
                        self.calc_moves(pawn, clicked_row, clicked_col)
                        self.dragger.save_initial(event.pos) # Saves the initial position of the pawn
                        self.dragger.drag_pawn(pawn)
                        self.show_moves(self.screen)
                    
                    

            if event.type == py.MOUSEMOTION:
                # If we are dragging the pawn
                if self.dragger.dragging:
                    self.dragger.update_mouse(event.pos)
                    self.show_moves(self.screen)
                    self.dragger.update_screen(self.screen)

            if event.type == py.MOUSEBUTTONUP:
                if self.dragger.dragging:
                    self.dragger.update_mouse(event.pos)

                released_row = self.dragger.pos_y // utils.SQSIZE
                released_col = self.dragger.pos_x // utils.SQSIZE

                # Create possible move
                initial = Case(self.dragger.initial_row, self.dragger.initial_col)
                final = Case(released_row, released_col)
                move = Move(initial, final)

                # Checks if it is a valid move
                if self.valid_move(self.dragger.pawn, move): # I stopped there, the valid move verification has an issue. I think it is most likely that the move isn't considered a valide one thus is not accepted, you should look more into it
                # print('test successful')
                    if self.dragger.pawn != None:
                        self.move_pawn(self.dragger.pawn, move)
                        self.turn(4) # You should really use a variable here

                self.dragger.undrag_pawn()
                

    def turn(self, number):

        if number == 2:
            if self.player== "white":
                self.player = "red"
            else: self.player = "white"

        if number == 3:
            if self.player == "white":
                self.player = "red"
            
            elif self.player == "red": self.player = "green"
            else:
                self.player = "white"

        if number == 4:
            if self.player == "white":
                self.player = "red"

            elif self.player == "red":
                self.player = "green"
            
            elif self.player == "green": self.player = "black"
            else:
                self.player = "white"
        


    # Game loop
    def mainloop(self):
        # The dropdown lists don't work
        board_sizes = Dropdown(
            self.screen,
            200,  # x
            200,  # y
            100,  # width
            50,  # height
            "This is a test",
            ["5x5", "7x7", "9x9", "11x11"],
            eventType=py.MOUSEBUTTONDOWN
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
                py.display.set_caption(f'QUORRIDOR! {self.player}\'s turn')  # sets the screen title
                self.show_board(self.screen)
                self.show_moves(self.screen)
                self.show_walls(self.screen)
                self.show_pawns(self.screen)

                if self.dragger.dragging:
                    self.dragger.update_screen(self.screen)

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
