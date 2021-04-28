from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def circumference(self):
        return 2 * self.radius * pi


if __name__ == '__main__':
    circle = Circle(1)
    print(circle.circumference())

