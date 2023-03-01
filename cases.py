import utils
import pygame

class Case:

    def __init__(self, row, col, pawn=None, fence=None):
        self.row = row
        self.col = col
        self.pawn = pawn
        self.fence = fence
        self.moves()
        



    def moves(self):
        # self.clicked = False
        # # if self.pawn != None:
        # if pygame.MOUSEBUTTONDOWN and not self.clicked:
        #         print('round-about')
        #         Case(self.row, self.col)
                pass

    def has_pawn(self):
        return self.pawn != None

    def draw_fence(self):
        pass

    def has_fence(self):
        return self.fence != None

