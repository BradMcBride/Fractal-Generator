def PixelColor(ComplexNum, PaletteLen):
    julianConstant = complex(0.5667, 0.0)
    phoenixConstant = complex(-0.5, 0.0)
    cFlipped = complex(ComplexNum.imag, ComplexNum.real)
    cPrev = 0 + 0j
    ComplexNum = cFlipped
    PaletteLen = PaletteLen - 1     # This changes the length of a list to be used in calling certain indexes.
    for iter in range(PaletteLen):
        cSave = ComplexNum
        ComplexNum = ComplexNum * ComplexNum + julianConstant + (phoenixConstant * cPrev)
        cPrev = cSave
        if abs(ComplexNum) > 2:
            return iter
    return PaletteLen