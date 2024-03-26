import unittest
from shapes import Circle, Triangle

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(circle.calculate_area(), 78.54)

    def test_triangle_area(self):
        triangle = Triangle(side1=3, side2=4, side3=5)
        self.assertAlmostEqual(triangle.calculate_area(), 6.0)

    def test_right_angled_triangle(self):
        triangle = Triangle(side1=5, side2=12, side3=13)
        self.assertTrue(triangle.is_right_angled())

if __name__ == '__main__':
    unittest.main()
