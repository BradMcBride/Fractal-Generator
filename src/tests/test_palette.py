import unittest
from Palette import MbrotPalette, PhoenixPalette


class TestPalette(unittest.TestCase):
    def test_gradientLengthPhoenix(self):
        """Color palette contains the expected number of colors"""
        self.assertEqual(102, len(PhoenixPalette))

    def test_paletteLengthMandelbrot(self):
        """Palette contains the expected number of colors"""
        self.assertEqual(111, len(MbrotPalette))

    def test_paletteIsAllStrings(self):
        for color in PhoenixPalette:
            self.assertTrue(isinstance(color, str))
        for color in MbrotPalette:
            self.assertTrue(isinstance(color, str))

if __name__ == '__main__':
    unittest.main()