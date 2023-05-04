import pygame
from pygame.locals import *

SIZE = 500, 200
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # screen.fill(GRAY)
    for x in range(5):
        for y in range(5):
            rect = Rect(x * (500//8), y * (500//8), 200, 80)
            pygame.draw.rect(screen, 'blue', rect)
            pygame.display.flip()

pygame.quit()
