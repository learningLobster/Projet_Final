from pygame import mixer
from game import Menu


def main():
    """
    This function executes the entire code with all classes.
    """
    mixer.init()
    game = Menu()
    game.mainloop()


if __name__ == '__main__':
    main()
