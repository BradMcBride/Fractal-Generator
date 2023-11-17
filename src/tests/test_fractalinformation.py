import unittest
from FractalInformation import FractalInformation

class TestFractalInformation(unittest.TestCase):
    def test_dictionaryTester(self):
        """Names of fractals in the configuration dictionary are as expected"""

        self.assertNotIn('absent', FractalInformation)
        self.assertIn('phoenix', FractalInformation)
        self.assertNotIn('', FractalInformation)
        self.assertIn('peacock', FractalInformation)
        self.assertNotIn('Still Not In Here', FractalInformation)
        self.assertIn('monkey-knife-fight', FractalInformation)
        self.assertNotIn('shrimp-coctail', FractalInformation)
        self.assertIn('shrimp-cocktail', FractalInformation)

    def test_fractalInformationIsAccurate(self):
        self.assertEqual(FractalInformation['phoenix']['fractalType'], 'phoenix')
        self.assertEqual(FractalInformation['leaf']['fractalType'], 'mandelbrot')
        self.assertEqual(FractalInformation['mandelbrot']['fractalType'], 'mandelbrot')
        self.assertEqual(FractalInformation['peacock']['axisLen'], 0.0840187115019564)
        self.assertEqual(FractalInformation['monkey-knife-fight']['centerX'], -0.945542168674699)
        self.assertEqual(FractalInformation['seahorse']['centerY'], -0.102)
        self.assertNotEqual(FractalInformation['spiral1']['fractalType'], 'phoenix')
        self.assertNotEqual(FractalInformation['starfish']['centerX'], 0)
        self.assertNotEqual(FractalInformation['phoenix']['fractalType'], 'mandelbrot')


if __name__ == '__main__':
    unittest.main()