class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

r = Rectangle(10, 5)
print("Area:", r.area())