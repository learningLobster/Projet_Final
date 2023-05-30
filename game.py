# Pygame and other modules
import pygame as py
from pygame import mixer
import sys
import pygame_widgets
from pygame_widgets.dropdown import Dropdown
import pyautogui as popup # This module is used to display Pop-ups # For some reason it shrinks the game window



# Project files
import menu_button as button
import colours
from cases import Case
from pawn import Pawn
from dragger import Dragger



class Move:

    def __init__(self, initial, final):
        # initial and final are cases
        self.initial = initial
        self.final = final

    def __eq__(self, other):  # What is a dunder method? This functoin compares two moves
        return self.initial == other.initial and self.final == other.final




class Menu():

    def __init__(self):

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        # Create game Window
        py.init()  # It is imperative to put this in the code, because it initializes all pygame modules
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set the screen dimensions

        # Game state variable
        self.game_state = 'menu'

        py.display.set_caption('Quorridor')  # sets the window title
        game_icon = py.image.load('assets\\Pictures\\game_icon.png') # Loads an Image
        py.display.set_icon(game_icon) # sets the window icon
        self.clock = py.time.Clock() # What is that?

        # Load button images
        help_img = py.image.load("assets\\Pictures\\help_button.png").convert_alpha()
        quit_img = py.image.load("assets\\Pictures\\quit_button.png").convert_alpha()
        start_img = py.image.load("assets\\Pictures\\start_button.png").convert_alpha()
        back_img = py.image.load("assets\\Pictures\\back_button.png").convert_alpha()
        resume_img = py.image.load("assets\\Pictures\\resume_button.png").convert_alpha()
        proceed_img = py.image.load("assets\\Pictures\\proceed_button.png").convert_alpha()

        # create button instances
        self.start_button = button.Button(
            self.width_prct(40),  # x position
            self.height_prct(25),  # y position
            start_img,  # The image
        )

        self.help_button = button.Button(
            self.width_prct(40),
            self.height_prct(45),
            help_img,  # The image
        )

        self.quit_button = button.Button(
            self.width_prct(40),
            self.height_prct(65),
            quit_img,
        )

        self.back_button = button.Button(
            self.width_prct(60),  # x coordinate
            self.height_prct(85),  # y coordinate
            back_img,
        )

        self.resume_button = button.Button(
            self.width_prct(25),
            self.height_prct(85),
            resume_img,
        )
        
        self.proceed_button = button.Button(
            self.width_prct(25),
            self.height_prct(86),
            proceed_img,
        )


        # Dropdowns
        self.board_size = Dropdown(
            self.screen,
            self.width_prct(30),
            self.height_prct(10),
            width=350,
            height=50,
            name = 'Selects the board size(taille du plateau)',
            choices=['5x5', '7x7', '9x9', '11x11'],
            borderRadius = 3,
            colour = py.Color('beige'),
            values=[5, 7, 9, 11],
            direction='down',
        )
        self.number_of_players = Dropdown(
            self.screen,
            self.width_prct(30),
            self.height_prct(35),
            width=350,
            height=50,
            name='Select the number of players(nombre de joueurs)',
            choices=['2', '3', '4'],
            borderRadius=3,
            colour=py.Color('beige'),
            values=[2, 3, 4],
            direction='down',
        )
        self.number_of_walls = Dropdown(
            self.screen,
            self.width_prct(30),
            self.height_prct(60),
            width=350,
            height=50,
            name='Select the number of walls(nombre de murs)',
            choices=['4', '20', '40'],
            borderRadius=3,
            colour=py.Color('beige'),
            values=[4, 20, 40],
            direction='down',
        )

    
    # The two functions below help us position elements onto the screen
    def height_prct(self, percentage):
        return (self.SCREEN_HEIGHT / 100) * percentage

    def width_prct(self, percentage):
        return (self.SCREEN_WIDTH / 100) * percentage


    def get_number_of_walls(self):
        pass
    
    # Sound methods
    def move_sound(self):
        sound_file = mixer.Sound("assets\\Sounds\\move_sound.wav")
        m_sound = mixer.Sound.play(sound_file)
        m_sound.set_volume(0.1)

    def theme_sound(self):
        mixer.music.load("assets\\Sounds\\Passing_Through.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)

    def game_over_sound(self):
        sound_file = mixer.Sound("assets\\Sounds\\gameover_sound.wav")
        mixer.Sound.play(sound_file).set_volume(0.3)

    def stop_theme_sound(self):
        mixer.music.stop()

    # Event handler
    def check_events(self):
        """
        TODO: Check every action made by the user on the computer.
        """
        for event in py.event.get():
            # Allows the user to quit the application correctly
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        

    def mainloop(self):
        running = True
        while running:
            self.check_events()
            self.screen.fill((250, 52, 25))  # Background color, use a theme color instead
            if self.game_state == "menu":
                if self.start_button.display(self.screen):
                    self.game_state = 'utils'
                if self.help_button.display(self.screen):
                    self.game_state = 'help'
                if self.quit_button.display(self.screen):
                    py.quit()
                    sys.exit()

            elif self.game_state == 'help': # Take care of this window as well
                self.screen.fill(colours.SPARE_COLOR)

                font = py.font.SysFont("comicsansms",55)
                text = font.render("""This game is called Quoridor. The rules are really simple:\n- First: Play\n- Second: Don't lose\n- Third: Win!""",
                True,
                'cyan',
                'white')
                
                text_rect = text.get_rect()
                text_rect.center = ((self.SCREEN_WIDTH//2),(self.SCREEN_HEIGHT//2))
                self.screen.blit(text, text_rect)

                if self.back_button.display(self.screen):
                    self.game_state = 'menu'

            elif self.game_state == 'utils':
                pygame_widgets.update(py.event.get())
                if self.back_button.display(self.screen):
                    self.game_state = 'menu'

                if self.proceed_button.display(self.screen):
                    self.game_state = 'game'

            elif self.game_state == 'game':
                if (self.board_size.getSelected(), self.number_of_players.getSelected(), self.number_of_walls.getSelected()) is not None:
                    print("I'm in!!!")
                    self.rows = self.board_size.getSelected()
                    self.cols = self.board_size.getSelected()
                    self.players = self.number_of_players.getSelected()
                    self.SQSIZE = (self.SCREEN_WIDTH // self.rows)
                    game = Quoridor(self.rows, self.cols, self.players, self.SQSIZE)

                else:
                    self.rows = 9
                    self.cols = 9
                    self.players = 2
                    self.SQSIZE = 89
                    print("Im out!!!")
                    game = Quoridor(self.rows, self.cols, self.players, self.SQSIZE)
                running = False
                game.mainloop()
            
            # self.clock.tick(60)
            py.display.update()


class Quoridor(Menu):
    """
    TODO: Execute the game logic
    """
    def __init__(self, rows, cols, NUM_OF_PLAYERS, SQSIZE):
        self.rows = rows
        self.cols = cols
        self.NUM_OF_PLAYERS = NUM_OF_PLAYERS
        self.SQSIZE = SQSIZE
        super().__init__()
        self.theme_sound()

        self.test = False # Est utilisée à des fins de test sur les barrières

        self.dragger = Dragger() # Instantiation of the Dragger class

        # This is my console board
        self.cases = [[0] * cols for i in range(cols)]
        # Turn squares into instances of another class(will serve to add some properties)
        for row in range(rows):
            for col in range(cols):
                # Will give to each square the properties of the Case class
                self.cases[row][col] = Case(row, col)

        # Game state variables
        # self.game_paused = False
        self.game_over = False
        
        # Turn management variables
        self.all_players = ["white", "red", "black", "green"]
        self.actual_players = []
        self.clicked = False
        self.idx = 0

        # Add player
        for number in range(NUM_OF_PLAYERS):
            self.actual_players.append(self.all_players[number])
        self.player = self.actual_players[self.idx]


        # Pawns colours
        P1 = colours.P1_COLOR
        P2 = colours.P2_COLOR
        P3 = colours.P3_COLOR
        P4 = colours.P4_COLOR

        # Move related variables
        self.last_move = None  # I don't think I'll need but it can be useful

        # Pawns
        self.white_pawn = Pawn(P1)
        self.red_pawn = Pawn(P2)
        self.black_pawn = Pawn(P3)
        self.green_pawn = Pawn(P4)

        # Load the pawn images
        self.red_piece = self.red_pawn.img.convert_alpha()
        self.white_piece = self.white_pawn.img.convert_alpha()
        self.black_piece = self.black_pawn.img.convert_alpha()
        self.green_piece = self.green_pawn.img.convert_alpha()

        # Position the pawns in the console board
        match(NUM_OF_PLAYERS):
            case 2:
                self.set_pawn_position(rows//2, -1, P1)
                self.set_pawn_position(rows//2, 0, P2)
            case 3:
                self.set_pawn_position(rows//2, -1, P1)
                self.set_pawn_position(rows//2, 0, P2)
                self.set_pawn_position(0, rows//2, P3)
            case 4:
                self.set_pawn_position(rows//2, -1, P1)
                self.set_pawn_position(rows//2, 0, P2)
                self.set_pawn_position(0, rows//2, P3)
                self.set_pawn_position(-1, rows//2, P4)



    # Set the postion of each pawn in the console board
    def set_pawn_position(self, row, col, color):
        """
        TODO: Set pawn position on the console board.
        Parameters: 
            row: the row position.
            col: The column position.
            color: The pawn color.
        Returns:
            A square object containing a pawn.
        """
        if color == "white": # P1
            self.cases[row][col] = Case(row, col, self.white_pawn)
        elif color == "red": # P2
            self.cases[row][col] = Case(row, col, self.red_pawn)
        elif color == "black": # P3
            self.cases[row][col] = Case(row, col, self.black_pawn)
        elif color == "green": # P4 # Or you can use an else statement
            self.cases[row][col] = Case(row, col, self.green_pawn)
        # return self.cases[row][col] # Do I need this return statement?


    # Defines the list of possible moves
    def define_moves(self, pawn, row, col): # Calc move works perfectly, at least it returns the right squares. It does return the right result
        """
        TODO: set a list of possible moves.
        PARAMETERS: 
            pawn: the pawn we wanrt to move.
            row: the pawn row.
            col: the pawn col.
        """
        
        # A set of all possible movements
        possible_moves = [
            (row, col-1),  # left
            (row, col+1),  # right
            (row-1, col),  # up
            (row+1, col)  # down
        ]
        
        for possible_move in possible_moves:
            possible_move_row, possible_move_col = possible_move

            # This exception will make sure that the pawns do not go out of the screen(don't exceed the board size).
            try:
                if self.cases[possible_move_row][possible_move_col].empty():
                    if not self.cases[possible_move_row][possible_move_col].has_pawn():
                        # Creates new cases
                        initial = Case(row, col)
                        final = Case(possible_move_row, possible_move_col)

                        # Create new move
                        move = Move(initial, final)
                        pawn.add_move(move)
                    
                else:
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
            except IndexError:
                print("TEST!!!!")


    # Moves pawns
    def move_pawn(self, pawn, move):
        """
        TODO: move a pawn.
        PARAMETERS: 
            pawn: the pawn being moved.
            move: the move we are trying to make.
        """
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
        """
        TODO: Check if a move is valid and prevent invalid ones.
        Parameters: 
            pawn: The pawn we want to move.
            move: The move we want to make(an instance of the move class).
        """
        if pawn is not None:
            return move in pawn.moves


    def save_initial(self, dragger, pos): # Initial position
        # Come up with a better formula and this will solve the problem
        dragger.initial_row = pos[1] // self.SQSIZE
        dragger.initial_col = pos[0] // self.SQSIZE


    # display methods

    # Displays board
    def display_board(self, screen):
        """
        TODO: Display the game board.
        Parameters:
            screen: The pygame surface.
        """
        screen.fill(colours.BOARD_COLOR)  # Board color (119, 154, 88)
        for row in range(self.rows):
            for col in range(self.cols):
                # Squares
                squares_rect = ( # rectangle dimensions, the format is (row, col, width, height)
                                col * self.SQSIZE,
                                row *self.SQSIZE, 
                                self.SQSIZE, 
                                self.SQSIZE) 
                squares = py.draw.rect(
                    screen, colours.WALLS_COLOR, squares_rect, 5, 5) # Lines colors
                
                # What was I using it for?(28/05/2023; 21:49). At the very first it was just a check, now it's used to implement walls
                pos = py.mouse.get_pos()
                if squares.collidepoint(pos):
                    if py.mouse.get_pressed()[0] == 1:
                        # print(pos)
                        row = pos[1] // self.SQSIZE
                        col = pos[0] // self.SQSIZE
                        # self.set_wall(self.screen, col, row)
                        # self.display_walls(self.screen)
                        # print(pos[1] // self.SQSIZE) # Row
                        # print(pos[0] // self.SQSIZE) # Col

    # def set_wall(self, screen, col, row):
    #     horiz_rect = (
    #     col * self.SQSIZE, 
    #     (row+1) * self.SQSIZE, 
    #     self.SQSIZE, 
    #     10
    #     )
    #     horizontal_walls = py.draw.rect(screen, "#331a00", horiz_rect, 1)
    # Displays walls
    def display_walls(self, screen):
        # test colors
        RED = (255, 0, 0)
        blc = (0, 0, 0)

        for row in range(self.rows-1):
            for col in range(self.cols-1):
                # Horizontal wall spots
                horiz_rect = (
                    col * self.SQSIZE, 
                    (row+1) * self.SQSIZE, 
                    self.SQSIZE, 
                    10
                    )
                horizontal_walls = py.draw.rect(screen, "#331a00", horiz_rect)

                # Vertical walls
                vert_rect = (
                    (col+1) * self.SQSIZE, 
                    (row-1) * self.SQSIZE, 
                    10, 
                    self.SQSIZE
                    )
                vert_walls = py.draw.rect(screen, "#331a00", vert_rect)

                # Click handler
                pos = py.mouse.get_pos()
                if horizontal_walls.collidepoint(pos) and self.clicked is False:
                    # and self.clicked == False:
                    if py.mouse.get_pressed()[0] == 1 and not self.dragger.dragging:
                        self.clicked = True
                        horizontal_walls = py.draw.rect(
                            screen, blc, horiz_rect, 1)

                if vert_walls.collidepoint(pos):
                    # and self.clicked == False:
                    if py.mouse.get_pressed()[0] == 1:
                        # self.clicked = True
                        vert_walls = py.draw.rect(screen, blc, vert_rect, 1)



    # Display pawns
    def display_pawns(self, screen):
        """
        TODO: display the pawns.
        Parameters:
            screen: pygame surface.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                # I position the pawns in this loop
                
                if self.cases[row][col].has_pawn():  # Check if the square has a pawn
                    pawn = self.cases[row][col].pawn

                    if pawn is not self.dragger.pawn:
                        # Draws(blits) the pawns and nothing else
                        img_rect = col * self.SQSIZE + self.SQSIZE // 2, \
                            row * self.SQSIZE + self.SQSIZE // 2  # Put the piece at the center of the square

                        if pawn.color == 'white':
                            white_img = self.white_pawn.img
                            white_rect = white_img.get_rect(center=img_rect)
                            screen.blit(
                                white_img,  # This is the image
                                white_rect
                            )
                            # white_rect.colliderect

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


    # Displays moves
    def display_moves(self, screen):
        """
        TODO: display the possible moves.
        Parameters: 
            screen: Pygame surface.        
        """
        if self.dragger.dragging:
            pawn = self.dragger.pawn

            # Loops all valid moves
            for move in pawn.moves:
                # color
                color = colours.MOVES_COLOR  # You should definitely change this color
                # rect
                rect = (
                        move.final.col * self.SQSIZE,
                        move.final.row *self.SQSIZE,
                        self.SQSIZE,
                        self.SQSIZE
                        )
                # blit
                py.draw.rect(screen, color, rect)

        
    def check_win(self, pawn, final):
        """
        TODO: check if a player has won.
        Parameters:
            pawn: The player's pawn.
            final: The final move. Basically the player's current position after his last move.
        """
        if final.row == 0 and pawn.color == 'green':
            print("Green wins!")
            self.cases[final.row][final.col].pawn = None # Erases the pawn from the screen
            popup.alert(text="Green wins", title="Game Message", button="Ok")
            self.actual_players.remove("green")

        elif final.row == (self.rows-1) and pawn.color == 'black':
            print(self.cases[final.row][final.col].pawn.color)
            self.cases[final.row][final.col].pawn = None # Erases the pawn from the screen
            popup.alert(text="Black wins", title="Game Message", button="Ok")
            self.actual_players.remove("black")

        elif final.col == (self.rows-1) and pawn.color == 'red':
            self.cases[final.row][final.col].pawn = None # Erases the pawn from the screen
            popup.alert(text="Red wins", title="Game Message", button="Ok")
            self.actual_players.remove("red")

        elif final.col == 0 and pawn.color == "white":
            self.cases[final.row][final.col].pawn = None # Erases the pawn from the screen
            popup.alert(text="White wins", title="Game Message", button="Ok")
            self.actual_players.remove("white")
    

    def check_game_over(self):
        """
        TODO: Check if a player has lost.
        """
        if len(self.actual_players) == 1:
            self.game_over = True
            self.game_over_sound()
            game_over_popup = popup.confirm(text=f"{self.player} loses! Do you wanna play again?", title="Game Over!", buttons=['Yes', 'No', 'Exit'])
            if game_over_popup == 'Yes':
                self.new_game()
            elif game_over_popup == 'Exit':
                py.quit()
                sys.exit()
            else:
                py.display.set_caption("Game Over! Press SPACE to play again.")
                self.stop_theme_sound()


    def new_game(self):
        """
        TODO: Make a new instance of the Game object. 
        """
        # How to make it work?
        r = self.rows
        c = self.cols
        p = self.NUM_OF_PLAYERS
        s = self.SQSIZE
        # Quoridor(r, c, p, s)
        self.__init__(r, c, p, s) # It kind of works but takes the user back to the very first window. My text formatter is not happy, look for a better way to do it


    # Event handler
    def check_events(self):
        """
        TODO: Check every action made by the user on the computer.
        """
        for event in py.event.get():
            # Allows to quit the application correctly
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            elif event.type == py.MOUSEBUTTONDOWN:

                self.test = True
                try:
                    self.dragger.update_mouse(event.pos) # update the mouse position
                    clicked_row = self.dragger.pos_y // self.SQSIZE # Returns the row that was clicked
                    clicked_col = self.dragger.pos_x // self.SQSIZE # Returns the column that was clicked
                    if self.cases[clicked_row][clicked_col].has_pawn(): # Checks wether the clicked cell has a pawn
                        pawn = self.cases[clicked_row][clicked_col].pawn # Stores the pawn from the clicked cell into the pawn variable

                        if pawn.color == self.player:
                            print(self.player)
                            self.define_moves(pawn, clicked_row, clicked_col)
                            self.save_initial(self.dragger, event.pos) # Saves the initial position of the pawn
                            self.dragger.drag_pawn(pawn)
                            self.display_moves(self.screen)
                            self.check_game_over()
                except IndexError:
                    print('Error!')
                    

            elif event.type == py.MOUSEMOTION:
                # Checks if we are dragging the pawn
                if self.dragger.dragging:
                    self.dragger.update_mouse(event.pos)
                    self.display_moves(self.screen)
                    self.dragger.update_screen(self.screen)

            elif event.type == py.MOUSEBUTTONUP:
                if self.dragger.dragging:
                    self.dragger.update_mouse(event.pos)

                released_row = self.dragger.pos_y // self.SQSIZE
                released_col = self.dragger.pos_x // self.SQSIZE

                # Create possible move
                initial = Case(self.dragger.initial_row, self.dragger.initial_col)
                final = Case(released_row, released_col)
                move = Move(initial, final) # It checks if the move we are trying to make is a valid one

                # Checks if it is a valid move
                if self.valid_move(self.dragger.pawn, move): # I stopped there, the valid move verification has an issue. I think it is most likely that the move isn't considered a valide one thus is not accepted, you should look more into it
                    if self.dragger.pawn is not None:
                        self.move_pawn(self.dragger.pawn, move)
                        self.check_win(self.dragger.pawn, final)
                        self.turn() # You should really use a variable here. I think it no longer requires a variablr=e(Must check)
                        # Move sound
                        self.move_sound()

                self.dragger.undrag_pawn()

            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    if self.game_over:
                        self.new_game()
                if event.key == py.K_h:
                    if not self.game_over:
                        self.rules()


    def rules(self):
        """
        TODO: Display the game rules.
        """
        # First prompt
        prompt = popup.confirm(text="which language do you speak?", title="Hello", buttons=["French", "English"])
        if prompt == "French":
            rules = popup.alert(text='Pour jouer, veuillez clicker sur le pion indiquer au haut de la fenêtre. Ce jeu est un jeu au tour par tour, durant chaque tour le pion est indiqué sur la fenêtre. Vous pouvez pouvez placer des barrières en cliquant sur les bordures du plateau.', title="Règles", button="OK!")
        elif prompt == "English":
            rules = popup.alert(text="You can play by dragging and dropping a pawn, as this is an in turn game, you will see the player whose turn it is at the top of the window. Fences can be placed by clicking on the board lines but be aware, their numbers are limited.", title="Rules", button="OK!")


    def turn(self):
        """
        TODO: Manage the change of turns. # It is not very clear.
        """
        self.idx += 1
        self.idx %= len(self.actual_players)  
        self.player = self.actual_players[self.idx]


    # Game loop
    def mainloop(self):
        """
        TODO: Call every function to make the game run.
        """

        while True:
            py.display.set_caption(f'QUORRIDOR! {self.player}\'s turn.' + "              " + "Press 'h' for rules/Cliquez sur 'h' pour les règles")  # sets the screen title
            self.check_events()            
            self.display_board(self.screen)
            self.display_moves(self.screen)
            # if self.test:
            #     self.display_walls(self.screen)
            self.display_pawns(self.screen)

            if self.dragger.dragging:
                self.dragger.update_screen(self.screen)

            self.clock.tick(60)
            py.display.update()


