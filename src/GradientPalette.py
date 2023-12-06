from Palette import Palette
import colour


class GradientPalette(Palette):
    def __init__(self, iteration):
        super().__init__(iteration)
        self._bigStone = '#334046'  # I was told I should use bigStone because the name sounded funny
        self._razzleDazzle = '#ff33cc'
        self._colorList = []

        for color in colour.Color(self._bigStone).range_to(self._razzleDazzle, self._iteration):
            self._colorList.append(color.hex_l)

    # def __init__(self, iteration):
    #     super().__init__(iteration)
    # bigStone = '#334046'  # I was told I should use bigStone because the name sounded funny
    # razzleDazzle = '#ff33cc'
    # colorList = []
    #
    # for color in colour.Color(bigStone).range_to(razzleDazzle, Palette.iteration):
    #     colorList.append(color.hex_l)

    def getColor(self, n):
        return self._colorList[n]