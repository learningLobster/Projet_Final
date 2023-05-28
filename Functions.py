from dragger import Dragger
import config
from cases import Case
from pawn import Pawn
from move import Move



class Game:
    def __init__(self):
        self.dragger = Dragger()

        # This is my console board
        self.cases = [[0] * config.COLS for i in range(config.COLS)]
        # Turn squares into instances of another class(will serve to add some properties)
        for row in range(config.ROWS):
            for col in range(config.COLS):
                # Will give to each square the properties of the Case class
                self.cases[row][col] = Case(row, col)

        # Game state variables
        # self.game_paused = False
        self.game_over = False
        self.game_state = 'menu'
        self.all_players = ["white", "red", "black", "green"]
        self.actual_players = []
        self.clicked = False

        # Pawns
        self.red_pawn = Pawn('red')
        self.white_pawn = Pawn('white')
        self.black_pawn = Pawn('black')
        self.green_pawn = Pawn('green')

        # # Load the pawn images(Display elements)
        # self.red_piece = self.red_pawn.img.convert_alpha()
        # self.white_piece = self.white_pawn.img.convert_alpha()
        # self.black_piece = self.black_pawn.img.convert_alpha()
        # self.green_piece = self.green_pawn.img.convert_alpha()

        # Position the pawns in the console board
        match(config.NUM_OF_PLAYERS):
            case 2:
                self.set_pawn_position(config.ROWS//2, 0, "red")
                self.set_pawn_position(config.ROWS//2, -1, "white")
            case 3:
                self.set_pawn_position(config.ROWS//2, 0, "red")
                self.set_pawn_position(config.ROWS//2, -1, "white")
                self.set_pawn_position(0, config.ROWS//2, "black")
            case 4:
                self.set_pawn_position(config.ROWS//2, 0, "red")
                self.set_pawn_position(config.ROWS//2, -1, "white")
                self.set_pawn_position(0, config.ROWS//2, "black")
                self.set_pawn_position(-1, config.ROWS//2, "green")

    
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

    
    # Defines possible moves
    def define_moves(self, pawn, row, col): # Calc move works perfectly, at least it returns the right squares. It does return the right result
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
                    

    # Moves pawns
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
    
