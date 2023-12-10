#!/usr/bin/env python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


import sys
import FractalInformation as FI
import PaletteFactory
import ImagePainter
import FractalParser
import FractalFactory

fractal = FractalFactory.makeFractal()
palette = PaletteFactory.make_colorPallete()
fractalInfo = {'type': 'mandelbrot', 'pixels': 640, 'iterations': 100, 'min': {'x': -2.0, 'y': -1.5}, 'max': {'x': 1.0, 'y': 1.5}}

if len(sys.argv) < 2:
    print("FractalFactory: Creating default fractal")

if len(sys.argv) == 2:
    print("PaletteFactory: Creating default fractal")

if len(sys.argv) >= 2:
    fileName = sys.argv[1]
    fractalInfo = FractalParser.fractalReader(fileName)
    fractal = FractalFactory.makeFractal(fractalInfo)
    palette = PaletteFactory.make_colorPallete("gradient", fractalInfo)

if len(sys.argv) == 3:
    paletteName = sys.argv[2]
    palette = PaletteFactory.make_colorPallete(paletteName, fractalInfo)


ImagePainter.main(fractal, palette, fractalInfo)