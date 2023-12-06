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

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for fractal in FI.FractalInformation:
        print(fractal)
    sys.exit(1)

colorPal = sys.argv[1]
palette = PaletteFactory.make_colorPallete()
print(palette.getColor(10))

# fractalChosen = sys.argv[1]
#
# if fractalChosen not in FI.FractalInformation:
#     print("ERROR:", sys.argv[1], "is not a valid fractal")  #
#     print("Please choose one of the following:")
#     for fractal in FI.FractalInformation:
#         print(fractal)
#     sys.exit(1)
#
# if fractalChosen in FI.FractalInformation:
#     ImagePainter.main(FI.FractalInformation[fractalChosen], fractalChosen)
