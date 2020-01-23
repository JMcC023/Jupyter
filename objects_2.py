import math

class Shape:
    def getArea(self):
        return None
        
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
    
    _pi = 3.14
    # This is a static variable that can be used by all member functions of this class
    
    def getArea(self):
        print("Pi = ", Circle._pi, self._pi)
        return math.sqrt(Circle._pi*self._radius*self._radius)
        
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth
    
    def getArea(self):
        return self._length * self._breadth

class Square(Rectangle):
    def __init__(self, side):
        self._length = side
        self._breadth = side
        
        # Note here, Square inherits from rectangle *not shape
        
# Instantiate shapes..
shape = Shape()
circle = Circle(4.5)
rectangle = Rectangle(4,5)
square = Square(5)

shapes = [shape, circle, rectangle, square]
for a_shape in shapes:
    print(a_shape.getArea())
