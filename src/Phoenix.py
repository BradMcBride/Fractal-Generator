# def getColorFromPalette(z):
#     """
#     Return the index of the color of the current pixel
#     within the Phoenix fractal in the palette array
#     """
#
#     # I feel bad about all of the global variables I'm using.
#     # There must be a better way...
#     global grad
#     global win
#
#     # c is the Julia Constant; varying this value gives rise to a variety of variated images
#     julianConstant = complex(0.5667, 0.0)
#
#     # phoenix is the Phonix Constant; same deal as above - adjust this to get different results
#     phonixConstant = complex(-0.5, 0.0)
#
#     # The first thing we do to the complex number Z is reflect its components,
#     # so the imaginary part becomes the real part, and vice versa
#     zFlipped = complex(z.imag, z.real)
#     ## if we don't do this, the image comes out SIDEWAYS!!!
#
#     # zPrevious is the PREVIOUS Z value, except the 1st time through the
#     # function, when it starts out as Complex Zero (which is actually the
#     # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!
#     zPrev = 0+0j
#     # set Z back to zFlipped, it is literally super-important that we do this
#     # before the next part of the algorithm
#     z = zFlipped
#
#     # I want to use 101 here because that's the number of colors in the
#     # palette.  Except range() wants its number to be one more than the number
#     # that YOU want.
#     for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?
#         zSave = z  # save the current Z value before we overwrite it
#         # compute the new Z value from the current and previous Zs
#         z = z * z + JulianConstant + (pheonix * zPrev)
#         zPrev = zSave  # Set the prevZ value for the next iteration
#         if abs(z) > 2:
#             return grad[i]  # The sequence is unbounded
#     return grad[101]         # Else this is a bounded sequence

def PixelColor(c, PaletteLen):
    julianConstant = complex(0.5667, 0.0)
    phonixConstant = complex(-0.5, 0.0)
    zFlipped = complex(c.imag, c.real)
    zPrev = 0 + 0j
    s = zFlipped
    PaletteLen = PaletteLen - 1     # This changes the length of a list to be used in calling certain indexes.
    for iter in range(PaletteLen):
        zSave = s
        s = s * s + julianConstant + (phonixConstant + zPrev)
        zPrev = zSave
        if abs(s) > 2:
            # if iter >= numberOfColors:
            #     iter = numberOfColors - 1
            return iter
    return PaletteLen