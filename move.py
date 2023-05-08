class Move:

    def __init__(self, initial, final):
        # initial and final are cases
        self.initial = initial
        self.final = final

    def __eq__(self, other):  # What is a dunder method?
        return self.initial == other.initial and self.final == other.final
