import sys
import Mandelbrot
import Phoenix
defaultDict = {'type': 'mandelbrot'}
def makeFractal(dict=defaultDict):
    if dict['type'] == "mandelbrot":
        fractal = Mandelbrot
    elif dict['type'] == "phoenix":
        fractal = Phoenix
    else:
        sys.exit(1)
    return fractal