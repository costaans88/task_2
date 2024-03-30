import unittest
from Figures.Triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_area(self):
        tri = Triangle(3, 4, 5)
        self.assertEqual(tri.area, 6.0)

    def test_is_right_triangle(self):
        tri1 = Triangle(3, 4, 5)
        tri2 = Triangle(5, 12, 13)
        tri3 = Triangle(9, 40, 41)
        self.assertTrue(tri1.is_right_triangle())
        self.assertTrue(tri2.is_right_triangle())
        self.assertTrue(tri3.is_right_triangle())


if __name__ == '__main__':
    unittest.main()