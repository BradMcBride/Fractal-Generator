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


import unittest
from Mandelbrot import Mandelbrot


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):
    def test_count(self):
        """Mandelbrot fractal configuration and algorithm output the expected colors index at key locations"""

        self.assertEqual(Mandelbrot.count(self, complex(0, 0), 110), 110)
        self.assertEqual(Mandelbrot.count(self, complex(-0.751, 1.1075), 110), 3)
        self.assertEqual(Mandelbrot.count(self, complex(-0.2, 1.1075), 110), 10)
        self.assertEqual(Mandelbrot.count(self, complex(-0.75, 0.1075), 110), 31)
        self.assertEqual(Mandelbrot.count(self, complex(-0.748, 0.1075), 110), 57)
        self.assertEqual(Mandelbrot.count(self, complex(-0.7562500000000001, 0.078125), 110), 39)
        self.assertEqual(Mandelbrot.count(self, complex(-0.7562500000000001, -0.234375), 110), 13)
        self.assertEqual(Mandelbrot.count(self, complex(0.3374999999999999, -0.625), 110), 11)
        self.assertEqual(Mandelbrot.count(self, complex(-0.6781250000000001, -0.46875), 110), 30)
        self.assertEqual(Mandelbrot.count(self, complex(0.4937499999999999, -0.234375), 110), 5)
        self.assertEqual(Mandelbrot.count(self, complex(0.3374999999999999, 0.546875), 110), 23)


if __name__ == '__main__':
    unittest.main()
