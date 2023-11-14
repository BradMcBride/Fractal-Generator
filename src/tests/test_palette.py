import unittest
from Palette import palette

class TestPalette(unittest.TestCase):
    def test_ColorPaletteLength(self):
        self.assertEqual(102, len(palette))

    def test_ColorPaletteIsString(self):
        for color in palette:
            self.assertEqual(color, str)

if __name__ == '__main__':
    unittest.main()