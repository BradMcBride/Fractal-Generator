def PixelColor(c, PaletteLen):
    z = complex(0, 0)
    PaletteLen = PaletteLen - 1     # This changes the length of a list to be used in calling certain indexes.
    for iter in range(PaletteLen):
        z = z * z + c
        if abs(z) > 2:
            # if iter >= numberOfColors:
            #     iter = numberOfColors - 1
            return iter
    return PaletteLen