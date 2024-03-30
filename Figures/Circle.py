import math


class Circle:

    def __init__(self, radius=0):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2