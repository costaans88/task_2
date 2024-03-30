class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2