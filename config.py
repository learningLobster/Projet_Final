from pygame import mixer

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


ROWS = 5
COLS = ROWS
SQSIZE = SCREEN_WIDTH // COLS
NUM_OF_PLAYERS = 2

mixer.init()

# PLAYERS = 0
# NUM_WALLS = 0


# Those functions help us position element onto the screen
def height_prct(percentage):
    return (SCREEN_HEIGHT / 100) * percentage


def width_prct(percentage):
    return (SCREEN_WIDTH / 100) * percentage


def get_number_of_walls():
    pass

def move_sound():
    sound_file = mixer.Sound("assets\\Sounds\\move_sound.wav")
    m_sound = mixer.Sound.play(sound_file)
    m_sound.set_volume(0.1)
    

def theme_sound():
    mixer.music.load("assets\\Sounds\\Passing_Through.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)



