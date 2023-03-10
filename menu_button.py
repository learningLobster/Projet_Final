import pygame

# Button class


class Button:
    def __init__(self, x, y, image):
        """
            Parameters: x, y, image
            x = x coordinate
            y = y coordinate
            image = image to be blitted
        """
        self.image = image
        # Get the rect of the image
        self.rect = image.get_rect()
        # The rect is basically the coordinates at which the image will be drawn by default they are (0,0). The rect also contains the dimensions of the image

        # So here I am telling pygame to the topleft corner of the image must be at coords (x,y)
        self.rect.topleft = (x, y)

        

    # Draws the button image
    def display(self, surface):
        """
            TODO: Draw the button image
            Parameters: surface
        """
        # Check if the image has been clicked
        self.clicked = False
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos() # Very interesting code here

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos): # What is collidepoint? I think it is when the mouse is over the image

            # Button has been clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # Button has not been clicked
        if pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, self.rect.topleft)

        return action
