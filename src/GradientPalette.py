from Palette import Palette
import colour


class GradientPalette(Palette):
    def __init__(self, iteration):
        super().__init__(iteration)
        self._bigStone = '#334046'  # I was told I should use bigStone because the name sounded funny
        self._razzleDazzle = '#ff33cc'
        self._colorList = []

        # This line of code checks for if the iteration count is odd
        # If it is odd, the palette length is going to be off without this code
        __isOdd = 0
        if iteration % 2 == 1:
            __isOdd = 1

        for color in colour.Color(self._bigStone).range_to(self._razzleDazzle, int(self._iteration / 2) + __isOdd):
            self._colorList.append(color.hex_l)
        for color in colour.Color(self._razzleDazzle).range_to('#000000', int(self._iteration / 2)):
            self._colorList.append(color.hex_l)

    def getColor(self, n):
        return self._colorList[n - 1]