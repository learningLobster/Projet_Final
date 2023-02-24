import pygame as py
import sys
import utils
import button


class Game():
    def __init__(self):
        # Create game Window
        py.init()

        self.screen = py.display.set_mode(
            (utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT))
        py.display.set_caption('Quorridor')
        self.clock = py.time.Clock()

        # Game variables
        self.game_paused = False
        self.menu_state = 'main'

        # Define font
        self.font = py.font.SysFont('arialbalck', 40)

        # Define colors
        self.TEXT_COLOR = (255, 255, 255)

        # Load button images
        resume_img = py.image.load("assets\\resume_button.png").convert_alpha()
        help_img = py.image.load("assets\\help_button.png").convert_alpha()
        quit_img = py.image.load("assets\\quit_button.png").convert_alpha()
        start_img = py.image.load("assets\\start_button.png").convert_alpha()
        back_img = py.image.load("assets\\back_button.png").convert_alpha()

        # create button instances
        self.resume_button = button.Button(
            utils.width_prct(30), utils.height_prct(5), resume_img, 1)
        self.help_button = button.Button(utils.width_prct(
            30), utils.height_prct(25), help_img, 1)
        self.quit_button = button.Button(utils.width_prct(
            30), utils.height_prct(45), quit_img, 1)
        self.start_button = button.Button(
            utils.width_prct(30), utils.height_prct(5), start_img, 1)
        self.back_button = button.Button(utils.width_prct(
            30), utils.height_prct(45), back_img, 1)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def check_events(self):
        for event in py.event.get():
            # Allows to quit the application correctly
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    self.game_paused = True
                    print('Pause')

    # Game loop
    def mainloop(self):
        running = True
        while running:

            self.screen.fill((52, 78, 91))
            self.check_events()

            # Check if the game is paused
            if self.game_paused == True:
                # Check menu state
                # if self.menu_state == 'main':
                   # draw pause screen buttons
                   # Simply means that the button has been clicked, returns a boolean
                    if self.resume_button.draw(self.screen):
                        self.game_paused = False

                    if self.help_button.draw(self.screen):  # Simply means that the button has been clicked, returns a boolean
                        pass

                    if self.quit_button.draw(self.screen):  # Simply means that the button has been clicked, returns a boolean
                        py.quit()
                        sys.exit()

                # check if the help menu is enabled
                # elif self.menu_state == 'help':
                #     #draw the rules
                #     self.draw_text("Rules", self.font, self.TEXT_COLOR, utils.width_prct(30), utils.height_prct(50))
                #     if self.back_button.draw(self.screen):
                #         self.menu_state = 'main'

            else:
                self.draw_text("Press SPACE to pause", self.font, self.TEXT_COLOR, utils.width_prct(
                    30), utils.height_prct(50))

            py.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    test = Game()
    test.mainloop()
