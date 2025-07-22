import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = math.pi * self.radius * 2
        return area
    

newCircle = Circle(24)
print(newCircle.get_area())