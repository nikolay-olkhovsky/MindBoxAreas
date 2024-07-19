import unittest
import areas
import math
import random

class Test_Areas(unittest.TestCase):
    def test_circleArea(self):
        self.assertEqual(areas.circleArea(0), 0)
        self.assertEqual(areas.circleArea(1), math.pi)
        randomR = random.random()
        self.assertEqual(areas.circleArea(randomR), math.pi * randomR**2)
        randomR = -random.random()
        self.assertRaises(ValueError, areas.circleArea, randomR)

    def test_triangleArea(self):
        self.assertEqual(areas.triangleArea(3,4,5), 6)
        self.assertEqual(areas.triangleArea(4,5,3), 6)
        self.assertEqual(areas.triangleArea(5,3,4), 6)
        self.assertEqual(areas.triangleArea(4,3,5), 6)
        self.assertEqual(areas.triangleArea(3,5,4), 6)
        self.assertEqual(areas.triangleArea(5,4,3), 6)
        self.assertRaises(ValueError, areas.triangleArea, 0, random.random(), random.random())
        self.assertRaises(ValueError, areas.triangleArea, random.random(), 0, random.random())
        self.assertRaises(ValueError, areas.triangleArea, random.random(), random.random(), 0)
        self.assertRaises(ValueError, areas.triangleArea, -random.random(), random.random(), random.random())
        self.assertRaises(ValueError, areas.triangleArea, random.random(), -random.random(), random.random())
        self.assertRaises(ValueError, areas.triangleArea, random.random(), random.random(), -random.random())
        self.assertRaises(ValueError, areas.triangleArea, 1, 2, 3)

if __name__ == '__main__':
    unittest.main()
    