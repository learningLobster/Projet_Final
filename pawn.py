import pygame
import os


class Pawn:
    def __init__(self, color, texture_rect=None):
        self.color = color

        # Path related variables
        self.img = pygame.image.load(f"assets/Pictures/{color}_pawn(1).png")

        self.texture = os.path.join(f"assets/Pictures/{color}_pawn(1).png") # How do I replace this code? It might actually be better
        self.texture_rect = texture_rect

        # Move related variables
        self.moves = []
        self.moved = False # is it actually important?


    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []





