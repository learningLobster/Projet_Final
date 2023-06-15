import pygame


class Wall:
    def __init__(self):
        # self.color = color

        # Path related variables
        self.vert_img = pygame.image.load("assets/Pictures/vert_wall.png")
        self.horiz_img = pygame.image.load("assets/Pictures/horiz_wall.png")

        # self.texture = os.path.join(f"assets/Pictures/{color}_pawn(1).png") # How do I replace this code? It might actually be better
        # self.texture_rect = texture_rect

