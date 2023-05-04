import pygame as py
import utils

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
        print('This is update mouse')

    def save_initial(self, pos): # Initial position
        self.initial_row = pos[1] // utils.SQSIZE
        self.initial_col = pos[1] // utils.SQSIZE

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
        screen.blit(img, img.get_rect(center=img_center))
        print('This is dragger')