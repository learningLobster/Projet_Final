import pygame as py
import config

class Dragger:
    def __init__(self):
        self.dragging = False
        self.pos_x = 0
        self.pos_y = 0
        self.initial_row = 0
        self.initial_col = 0
        self.pawn = None

    def update_mouse(self, pos): # Updates the cursor position in real-time
        self.pos_x, self.pos_y = pos # (xcor, ycor)

    def save_initial(self, pos): # Initial position
        # Come up with a better formula and this will solve the problem
        self.initial_row = pos[1] // config.SQSIZE
        self.initial_col = pos[0] // config.SQSIZE

    def drag_pawn(self, pawn):
        self.pawn = pawn
        self.dragging = True

    def undrag_pawn(self):
        self.pawn = None
        self.dragging = False

    # Blit methods
    def update_screen(self, screen): # Update image or blit

        # path of the image
        path = self.pawn.texture

        # Image
        img = py.image.load(path)

        # Rectangle
        img_center = (self.pos_x, self.pos_y) # Mouse coords
        self.pawn.texture_rect = img.get_rect(center=img_center)
        pawn_rect = self.pawn.texture_rect

        screen.blit(img, pawn_rect)