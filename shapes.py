import math

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def is_right_angled(self):
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
def calculate_area(shape):
    return shape.calculate_area()
