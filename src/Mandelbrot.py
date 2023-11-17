def PixelColor(complexNum, PaletteLen):
    z = complex(0, 0)
    PaletteLen = PaletteLen - 1     # This changes the length of a list to be used in calling certain indexes.
    for iter in range(PaletteLen):
        z = z * z + complexNum
        if abs(z) > 2:
            return iter
    return PaletteLen