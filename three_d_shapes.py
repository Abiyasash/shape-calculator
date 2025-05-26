import math


class Prism:
    def __init__(self, base_shape, height):
        self.base_shape = base_shape
        self.height = height

    def lateral_area(self):
        return self.base_shape.perimeter() * self.height

    def total_area(self):
        return self.lateral_area() + (2 * self.base_shape.area())

    def volume(self):
        return self.base_shape.area() * self.height


class Cube:
    def __init__(self, side):
        self.side = side

    def lateral_area(self):
        return 4 * math.pow(self.side, 2)

    def total_area(self):
        return 6 * math.pow(self.side, 2)

    def volume(self):
        return math.pow(self.side, 3)


class Pyramid:
    def __init__(self, base_shape, height, slant_height):
        self.base_shape = base_shape
        self.height = height
        self.slant_height = slant_height

    def lateral_area(self):
        return 0.5 * self.base_shape.perimeter() * self.slant_height

    def total_area(self):
        return self.lateral_area() + self.base_shape.area()

    def volume(self):
        return (self.base_shape.area() * self.height) / 3


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def lateral_area(self):
        return 2 * math.pi * self.radius * self.height

    def total_area(self):
        return self.lateral_area() + (2 * math.pi * math.pow(self.radius, 2))

    def volume(self):
        return math.pi * math.pow(self.radius, 2) * self.height


class Cone:
    def __init__(self, radius, height, slant_height):
        self.radius = radius
        self.height = height
        self.slant_height = slant_height

    def lateral_area(self):
        return math.pi * self.radius * self.slant_height

    def total_area(self):
        return self.lateral_area() * (math.pi * math.pow(self.radius, 2))

    def volume(self):
        return (math.pi * math.pow(self.radius, 2) * self.height) / 3


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def total_area(self):
        return 4 * math.pi * math.pow(self.radius, 2)

    def volume(self):
        return (4 * math.pi * math.pow(self.radius, 3)) / 3
