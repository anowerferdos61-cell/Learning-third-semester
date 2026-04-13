from math import pi
class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle("Circle1", 5)
rectangle = Rectangle("Rectangle1", 4, 6)
print(f"\n{circle.name} area: {circle.area():.2f}")
print(f"\n{rectangle.name} area: {rectangle.area():.2f}\n")