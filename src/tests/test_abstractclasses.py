import unittest
from Fractal import Fractal
from Palette import Palette


class AbstractClasses(unittest.TestCase):
    def test_abstract_fractal(self):
        """Test whether Fractal class is abstract"""
        with self.assertRaises(NotImplementedError):
            Fractal()

    def test_abstract_palette(self):
        """Test whether Palette class is abstract"""
        with self.assertRaises(NotImplementedError):
            Palette(100)


if __name__ == '__main__':
    unittest.main()
