class Palette:
    def __init__(self, iteration):
        if type(self) == Palette:
            raise NotImplementedError("You must inherit from Palette; don't try to make one!")
        self._iteration = iteration

    def getColor(self, integer):
        raise NotImplementedError("You must implement a getColor method to any Palette classes!")
