from pygame import mixer
from game import Menu, Quoridor


def main():
    """
    This function executes the entire code with all classes.
    """
    mixer.init()
    # game = Menu()
    # game.mainloop()
    game = Quoridor(5, 5, 2, 88)
    game.mainloop()


if __name__ == '__main__':
    main()
