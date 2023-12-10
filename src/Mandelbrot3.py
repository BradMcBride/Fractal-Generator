from Fractal import Fractal

class Mandelbrot3(Fractal):
    def count(self, c, iter):
        z = complex(0, 0)
        for num in range(iter - 1):
            z = z * z * z + c
            if abs(z) > 2:
                return num + 1
        return iter