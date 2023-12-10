import unittest
from IntergalacticPalette import IntergalacticPalette
from GradientPalette import GradientPalette
from RandomPalette import RandomPalette


class TestPalette(unittest.TestCase):
    """Test whether the palette creates the correct amount of colors"""
    def test_intergalacticLength(self):
        palette = IntergalacticPalette(100)
        self.assertIsInstance(palette.getColor(100), str)
        self.assertIsInstance(palette.getColor(0), str)
        with self.assertRaises(IndexError):
            self.assertNotIsInstance(palette.getColor(101), str)

        palette = IntergalacticPalette(101)
        self.assertIsInstance(palette.getColor(101), str)
        self.assertIsInstance(palette.getColor(0), str)
        with self.assertRaises(IndexError):
            self.assertNotIsInstance(palette.getColor(102), str)


    def test_gradientLength(self):
        palette = GradientPalette(100)
        self.assertIsInstance(palette.getColor(100), str)
        self.assertIsInstance(palette.getColor(0), str)
        with self.assertRaises(IndexError):
            self.assertNotIsInstance(palette.getColor(101), str)

        palette = GradientPalette(101)
        self.assertIsInstance(palette.getColor(101), str)
        self.assertIsInstance(palette.getColor(0), str)
        with self.assertRaises(IndexError):
            self.assertNotIsInstance(palette.getColor(102), str)

    def test_randomLength(self):
        palette = RandomPalette(100)
        self.assertIsInstance(palette.getColor(100), str)
        self.assertIsInstance(palette.getColor(0), str)
        with self.assertRaises(IndexError):
            self.assertNotIsInstance(palette.getColor(101), str)

        palette = RandomPalette(101)
        self.assertIsInstance(palette.getColor(101), str)
        self.assertIsInstance(palette.getColor(0), str)
        with self.assertRaises(IndexError):
            self.assertNotIsInstance(palette.getColor(102), str)

if __name__ == '__main__':
    unittest.main()