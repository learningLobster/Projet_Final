import pygame as py
import sys
import utils; import theme

py.init()
screen = py.display.set_mode((800,800))
py.display.set_caption('Test Window')
screen.fill(theme.board_color)

def show_board(screen):
    for row in range(utils.ROWS):
        for col in range(utils.COLS):
            rect = (col * utils.SQSIZE, row * utils.SQSIZE,
                    utils.SQSIZE, utils.SQSIZE)  # rectangle dimensions
            
            py.draw.rect(screen, 'red', rect, 1, border_radius=5)
            

def mainloop():
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
                py.quit()
        
        show_board(screen)

        py.display.update()

mainloop()
