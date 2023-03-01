import pygame

# Button class


class Button:
    def __init__(self, x, y, image, scale):
        # Get the width and height of the image
        width = image.get_width()
        height = image.get_height()

        # Transforms the scale of the image
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        # I'm not sure if this this does
        self.rect = self.image.get_rect()

        # What is it used for?
        self.rect.topleft = (x, y)

        # Check if the image has been clicked
        self.clicked = False

    # Draws the button image
    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos() # Very interesting code here

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos): # What is collidepoint?

            # Button has been clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # Button has not been clicked
        if pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
