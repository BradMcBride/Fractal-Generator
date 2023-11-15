def PixelColor(c):

    z = complex(0, 0)  # z0

    numberOfColors = 111
    numberOfColors = numberOfColors - 1
    for iter in range(numberOfColors):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:
            # if iter >= numberOfColors:
            #     iter = numberOfColors - 1
            return iter
    return numberOfColors