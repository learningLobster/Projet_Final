# Each square of the board is an instance of this class, thus the move methods will be coded here.

import utils
import pygame

class Case:

    def __init__(self, row, col, pawn=None, fence=None):
        self.row = row
        self.col = col
        self.pawn = pawn
        self.fence = fence


    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    
    # Check if there is a pawn
    def has_pawn(self):
        return self.pawn != None # Returns True or False

    # check if there is a fence
    def has_fence(self): # Currenctly fences are being drawn directly onto the screen, try to move it to this function instead
        return self.fence != None
    
    def has_enemy(self, color): # This function doesn't work properly I think
        return self.has_pawn() and self.pawn.color != color # If the pawn color is different from the color parameter

    def empty(self):
        return not self.has_pawn()

    def empty_or_ennemy(self, color):
        return self.empty() or self.has_enemy(color)
        
    
    # When moving a piece it tells us the possible square inside the board
    @staticmethod # A static method is a method that lets us access the methods inside a class without having an instance of that said class
    def in_range(*args):  # *args tells python that this method can recive as many arguments as necessary
        for arg in args:
            if arg < 0 or arg > utils.ROWS-1:               
                return False
        return True

