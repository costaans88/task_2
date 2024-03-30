import unittest
from Figures.Circle import Circle
import math


class TestCircle(unittest.TestCase):
    def test_area_with_radius_0(self):
        circle = Circle(0)
        self.assertEqual(circle.area, 0)

    def test_area_with_radius_1(self):
        circle = Circle(1)
        self.assertEqual(circle.area, math.pi)

    def test_area_with_radius_5(self):
        circle = Circle(5)
        self.assertEqual(circle.area, 25 * math.pi)


if __name__ == 'main':
    unittest.main()