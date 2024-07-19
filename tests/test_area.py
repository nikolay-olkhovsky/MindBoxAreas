import unittest
from area import area
import math
import random

class Test_Area(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(1, type='circle'), math.pi)
        self.assertEqual(area(3, 4, 5, type='triangle'), 6)
        self.assertRaises(ValueError, area, 5, 6, type='rectangle')
        self.assertRaises(ValueError, area, type='circle')
        self.assertRaises(ValueError, area, 2, 3, type='circle')
        self.assertRaises(ValueError, area, 2, 3, 4, type='circle')
        self.assertRaises(ValueError, area, 5, type='rectangle')
        self.assertRaises(ValueError, area, type='rectangle')
        self.assertRaises(ValueError, area, 5, 6, 7, type='rectangle')
        self.assertRaises(ValueError, area, 3, 4, type='triangle')
        self.assertRaises(ValueError, area, 3, type='triangle')
        self.assertRaises(ValueError, area, type='triangle')
        self.assertRaises(ValueError, area, 3, 4, 5, 6, type='triangle')

if __name__ == '__main__':
    unittest.main()
 