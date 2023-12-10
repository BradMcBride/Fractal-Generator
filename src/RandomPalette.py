from Palette import Palette
import colour
from random import choice

class RandomPalette(Palette):
    def __init__(self, iteration):
        super().__init__(iteration)

        self._colorList = []
        __color1 = RandomPalette.randColor(self)
        __color2 = RandomPalette.randColor(self)
        __color3 = RandomPalette.randColor(self)

        # This line of code checks for if the iteration count is odd
        # If it is odd, the palette length is going to be off without this code
        __isOdd = 0
        if iteration % 2 == 1:
            __isOdd = 1

        for color in colour.Color(__color1).range_to(__color2, int(self._iteration / 2) + __isOdd):
            self._colorList.append(color.hex_l)
        for color in colour.Color(__color2).range_to(__color3, int(self._iteration / 2)):
            self._colorList.append(color.hex_l)


    def getColor(self, n):
        return self._colorList[n - 1]

    def randColor(self):
        hexList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
        randColor = ""
        for i in range(6):
            randColor = randColor + str(choice(hexList))
        randColor = '#' + randColor
        return randColor