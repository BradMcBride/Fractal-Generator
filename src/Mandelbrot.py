def PixelColor(c, iter):
    z = complex(0, 0)
    for num in range(iter):
        z = z * z + c
        if abs(z) > 2:
            return iter
    return num