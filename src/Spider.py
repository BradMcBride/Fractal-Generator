from Fractal import Fractal

class Spider(Fractal):
    def count(self, c, iter):
        z = complex(0, 0)
        for num in range(iter - 1):
            z = z * z + c
            c = c/2 + z
            if abs(z) > 2:
                return num + 1
        return iter