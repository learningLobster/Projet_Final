import pygame
import os


class Pawn:
    def __init__(self, color):
        self.color = color
        self.piece = pygame.image.load(f"assets\{color}_pawn(1).png")

        self.texture = os.path.join(f"assets\{color}_pawn(1).png") # How do I replace this code?





