class Fractal:
    def __init__(self):
        if type(self) == Fractal:
            raise NotImplementedError("You must inherit from Fractal; don't try to make one!")

    def count(self, number, iter):
        raise NotImplementedError("You must implement a count method to any Fractal classes!")