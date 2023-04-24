import pygame


class Pawn:
    def __init__(self, color):
        # self.color = color

        self.piece = pygame.image.load(f"assets\{color}_pawn(1).png")

test = Pawn('red')


