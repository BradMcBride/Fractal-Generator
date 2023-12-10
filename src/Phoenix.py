from Fractal import Fractal

class Phoenix(Fractal):
    def count(self, C, iter):
        julianConstant = complex(0.5667, 0.0)
        phoenixConstant = complex(-0.5, 0.0)
        cFlipped = complex(C.imag, C.real)
        cPrev = 0 + 0j
        C = cFlipped
        for num in range(iter - 1):
            cSave = C
            C = C * C + julianConstant + (phoenixConstant * cPrev)
            cPrev = cSave
            if abs(C) > 2:
                return num + 1
        return iter