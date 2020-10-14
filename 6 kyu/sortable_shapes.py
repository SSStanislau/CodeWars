'''
Although shapes can be very different by nature, they can be sorted by the size of their area.

Task:

Create different shapes that can be part of a sortable list. The sort order is based on the size of their respective areas:
The area of a Square is the square of its side
The area of a Rectangle is width multiplied by height
The area of a Triangle is base multiplied by height divided by 2
The area of a Circle is the square of its radius multiplied by π
The area of a CustomShape is given

The default sort order of a list of shapes is ascending on area size:
'''


from math import pi

class Shape(object):
    def __lt__(self, other):
        return self.area < other.area

class Square(Shape):
    def __init__(self, side):
        self.area = side * side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.area = width * height

class Triangle(Shape):
    def __init__(self, width, height):
        self.area = width * height / 2.0

class Circle(Shape):
    def __init__(self, radius):
        self.area = pi * radius ** 2
        
class CustomShape(Shape):
    def __init__(self, area):
        self.area = area
        
