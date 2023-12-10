from Palette import Palette
import colour


class IntergalacticPalette(Palette):
    def __init__(self, iteration):
        super().__init__(iteration)
        self._purple = '#90599a'
        self._teal = '#063f61'
        self._black = '#000000'
        self._colorList = []

        for color in colour.Color(self._black).range_to(self._black, int(self._iteration / 2) + 1):
            self._colorList.append(color.hex_l)
        for color in colour.Color(self._teal).range_to(self._purple, int(self._iteration / 2)):
            self._colorList.append(color.hex_l)

    def getColor(self, n):
        return self._colorList[n - 1]