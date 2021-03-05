from math import pi


class Circle:
    def __init__(self, radius):
        self.r = radius

    def get_circumference(self):
        return 2 * pi * self.r

    def get_area(self):
        return pi * self.r ** 2


if __name__ == '__main__':
    radius = eval(input('Enter the value of the radius: '))
    circle = Circle(radius)
    print('Circumference: ', round(circle.get_circumference()))
