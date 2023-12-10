import unittest
from ImagePainter import pixelsWrittenSoFar


class TestImagePainter(unittest.TestCase):
    def test_pixelsWrittenSoFar(self):
        """Progress bar produces correct output"""

        self.assertEqual(pixelsWrittenSoFar(1, 512), '[100% =================================]')
        self.assertEqual(pixelsWrittenSoFar(7, 512), '[ 99% =================================]')
        self.assertEqual(pixelsWrittenSoFar(257, 512), '[ 50% ================                 ]')
        self.assertEqual(pixelsWrittenSoFar(256, 512), '[ 50% =================                ]')
        self.assertEqual(pixelsWrittenSoFar(100, 512), '[ 80% ===========================      ]')
        self.assertEqual(pixelsWrittenSoFar(640, 512), '[-25%                                  ]')
        self.assertEqual(pixelsWrittenSoFar(137, 512), '[ 73% ========================         ]')
        self.assertEqual(pixelsWrittenSoFar(512, 512), '[  0%                                  ]')

if __name__ == '__main__':
    unittest.main()