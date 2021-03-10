import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        gcd = math.gcd(numerator, denominator)
        self.numerator = abs(numerator // gcd)
        self.denominator = abs(denominator // gcd)
        if (numerator < 0) ^ (denominator < 0):
            self.numerator = self.numerator * -1

    def __str__(self):
        return '{0}/{1}'.format(self.numerator, self.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == self.denominator

    def __add__(self, other):
        new_denominator = math.lcm(self.denominator, other.denominator)
        new_numerator = new_denominator // self.denominator * self.numerator + new_denominator // other.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_denominator = math.lcm(self.denominator, other.denominator)
        new_numerator = new_denominator // self.denominator * self.numerator - new_denominator // other.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __iadd__(self, other):
        new_denominator = math.lcm(self.denominator, other.denominator)
        new_numerator = new_denominator // self.denominator * self.numerator + new_denominator // other.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __isub__(self, other):
        new_denominator = math.lcm(self.denominator, other.denominator)
        new_numerator = new_denominator // self.denominator * self.numerator - new_denominator // other.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __lt__(self, other):
        pass



if __name__ == '__main__':
    f1 = Fraction(2, 3)
    f2 = Fraction(-1, 6)
    print(f1)
    print(f2)
    f1 += f2
    print(f1 != f2)