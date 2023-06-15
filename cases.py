# Each square of the board is an instance of this class, thus the move methods will be coded here.


class Case:

    def __init__(self, row, col, pawn=None, vert_fence=False, horiz_fence=False):
        self.row = row
        self.col = col
        self.pawn = pawn
        self.vert_fence = vert_fence
        self.horiz_fence = horiz_fence
        self.fence_activated = False


    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


    # Check if there is a pawn
    def has_pawn(self):
        return self.pawn is not None # Returns True or False


    # check if there is a fence
    def has_fence(self): # Currenctly fences are being drawn directly onto the screen, try to move it to this function instead
        return self.fence_activated is True


    def has_enemy(self, color): # This function doesn't work properly I think
        # Checks if the pawn color is different from the color parameter
        return self.has_pawn() and self.pawn.color != color


    def empty(self):
        return not self.has_pawn()


    # def empty_or_ennemy(self, color):
    #     return self.empty() or self.has_enemy(color)
