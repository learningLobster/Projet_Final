import utils
import pygame

class Case:

    def __init__(self, row, col, pawn=None, fence=None):
        self.row = row
        self.col = col
        self.pawn = pawn
        self.fence = fence
        self.moves()
        


    # Will make the moves
    def moves(self):
        pass

    # Calculates the possible
    def calc_moves(self):
        pass
    
    # Check if there is a pawn
    def has_pawn(self):
        return self.pawn != None

    # Draw  fence
    def draw_fence(self):
        pass

    # check if there is a fence
    def has_fence(self):
        return self.fence != None

