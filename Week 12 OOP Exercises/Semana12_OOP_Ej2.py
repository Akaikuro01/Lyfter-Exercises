from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle is: {perimeter}")

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        print(f"The area of the circle is: {area}")



class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = self.side * 4
        print(f"The perimeter of the square is: {perimeter}")

    def calculate_area(self):
        area = self.side ** 2
        print(f"The area of the square is: {area}")



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"The perimeter of the rectangle is: {perimeter}")

    def calculate_area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is: {area}")
    

circle = Circle(32)
circle.calculate_area()
circle.calculate_perimeter()

square = Square(40)
square.calculate_area()
square.calculate_perimeter()

rectangle = Rectangle(45, 35)
rectangle.calculate_perimeter()
rectangle.calculate_area()