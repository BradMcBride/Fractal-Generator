import sys
from Mandelbrot import Mandelbrot
from Phoenix import Phoenix
from Mandelbrot3 import Mandelbrot3
from Spider import Spider
defaultDict = {'type': 'mandelbrot'}
def makeFractal(dict=defaultDict):
    if dict['type'] == "mandelbrot":
        fractal = Mandelbrot()
    elif dict['type'] == "phoenix":
        fractal = Phoenix()
    elif dict['type'] == "mandelbrot3":
        fractal = Mandelbrot3()
    elif dict['type'] == "spider":
        fractal = Spider()
    else:
        sys.exit(1)
    return fractal