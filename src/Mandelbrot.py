from Fractal import Fractal

class Mandelbrot(Fractal):
    def count(self, c, iter):
        z = complex(0, 0)
        for num in range(iter - 1):
            z = z * z + c
            if abs(z) > 2:
                return num + 1 # The plus one makes it look slightly different (no circle around Mandelbrot)
        return iter