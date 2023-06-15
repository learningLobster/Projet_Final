import os
import pygame


class Pawn:
    def __init__(self, color):
        # self.color = color

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "assets", f"{color}_pawn(1).png")
        self.piece = pygame.image.load(image_path)

    def show_moves(self):
        pass

    def move_clicked(self):
        pass


test = Pawn('red')


