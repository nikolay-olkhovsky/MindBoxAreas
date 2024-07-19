import unittest
import figure
import math
import random

class Test_Figure(unittest.TestCase):
    def test_circle(self):
        self.assertEqual(figure.circle(0), 0)
        self.assertEqual(figure.circle(1), math.pi)
        randomR = random.random()
        self.assertEqual(figure.circle(randomR), math.pi * randomR**2)
        randomR = -random.random()
        self.assertRaises(ValueError, figure.circle, randomR)

    def test_triangle(self):
        self.assertEqual(figure.triangle(3,4,5), 6)
        self.assertEqual(figure.triangle(4,5,3), 6)
        self.assertEqual(figure.triangle(5,3,4), 6)
        self.assertEqual(figure.triangle(4,3,5), 6)
        self.assertEqual(figure.triangle(3,5,4), 6)
        self.assertEqual(figure.triangle(5,4,3), 6)
        self.assertRaises(ValueError, figure.triangle, 0, random.random(), random.random())
        self.assertRaises(ValueError, figure.triangle, random.random(), 0, random.random())
        self.assertRaises(ValueError, figure.triangle, random.random(), random.random(), 0)
        self.assertRaises(ValueError, figure.triangle, -random.random(), random.random(), random.random())
        self.assertRaises(ValueError, figure.triangle, random.random(), -random.random(), random.random())
        self.assertRaises(ValueError, figure.triangle, random.random(), random.random(), -random.random())
        self.assertRaises(ValueError, figure.triangle, 1, 2, 3)

if __name__ == '__main__':
    unittest.main()
    