SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# You should make getters and setters instead
ROWS = 9
COLS = 9
SQSIZE = SCREEN_WIDTH // COLS


def height_prct(percentage):
    return (SCREEN_HEIGHT / 100) * percentage


def width_prct(percentage):
    return (SCREEN_WIDTH / 100) * percentage
