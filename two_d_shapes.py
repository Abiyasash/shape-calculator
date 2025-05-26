import math


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return (2 * self.base) + (2 * self.height)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return math.pow(self.side, 2)

    def perimeter(self):
        return self.side * 4


class Parallelogram:
    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * (self.base + self.side)


class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

    def perimeter(self):
        return 4 * (math.sqrt(math.pow((self.diagonal1 / 2), 2) + math.pow((self.diagonal2 / 2), 2)))


class Trapezoid:
    def __init__(self, base1, base2, height, leg1, leg2):
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.leg1 = leg1
        self.leg2 = leg2

    def area(self):
        return 0.5 * self.height * (self.base1 + self.base2)

    def perimeter(self):
        return self.base1 + self.base2 + self.leg1 + self.leg2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def circumference(self):
        return 2 * math.pi * self.radius


class RegularPolygon:
    def __init__(self, apothem, side, num_sides):
        self.apothem = apothem
        self.side = side
        self.num_sides = num_sides

    def area(self):
        return 0.5 * self.apothem * self.perimeter()

    def perimeter(self):
        return self.side * self.num_sides
