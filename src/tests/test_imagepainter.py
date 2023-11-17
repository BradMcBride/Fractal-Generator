import unittest
from ImagePainter import pixelsWrittenSoFar


class TestImagePainter(unittest.TestCase):
    def test_pixelsWrittenSoFar(self):
        """Progress bar produces correct output"""

        self.assertEqual(pixelsWrittenSoFar(1), '[100% =================================]')
        self.assertEqual(pixelsWrittenSoFar(7), '[ 99% =================================]')
        self.assertEqual(pixelsWrittenSoFar(257), '[ 50% ================                 ]')
        self.assertEqual(pixelsWrittenSoFar(256), '[ 50% =================                ]')
        self.assertEqual(pixelsWrittenSoFar(100), '[ 80% ===========================      ]')
        self.assertEqual(pixelsWrittenSoFar(640), '[-25%                                  ]')
        self.assertEqual(pixelsWrittenSoFar(137), '[ 73% ========================         ]')
        self.assertEqual(pixelsWrittenSoFar(512), '[  0%                                  ]')

if __name__ == '__main__':
    unittest.main()