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
from Phoenix import Phoenix


class TestPhoenix(unittest.TestCase):
    def test_getPhoenixIteration(self):
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""
        self.assertEqual(Phoenix.count(self, complex(0, 0), 102), 6)
        self.assertEqual(Phoenix.count(self, complex(-0.751, 1.1075), 102), 1)
        self.assertEqual(Phoenix.count(self, complex(-0.2, 1.1075), 102), 2)
        self.assertEqual(Phoenix.count(self, complex(-0.750, 0.1075), 102), 35)
        self.assertEqual(Phoenix.count(self, complex(-0.748, -0.1075), 102), 102)
        self.assertEqual(Phoenix.count(self, complex(-0.75625, 0.078125), 102), 102)
        self.assertEqual(Phoenix.count(self, complex(-0.75625, -0.234375), 102), 33)
        self.assertEqual(Phoenix.count(self, complex(0.33749, -0.625), 102), 3)
        self.assertEqual(Phoenix.count(self, complex(-0.678125, -0.46875), 102), 102)
        self.assertEqual(Phoenix.count(self, complex(-0.406, -0.837), 102), 2)
        self.assertEqual(Phoenix.count(self, complex(-0.186, -0.685), 102), 3)


if __name__ == '__main__':
    unittest.main()
