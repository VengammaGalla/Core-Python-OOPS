from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def area(self):
        r = int(input("r: "))
        print((22/7)*r*r)

    def perimeter(self):
        r = int(input("r: "))
        print(2*(22/7)*r)

class Rectangle(Shape):
    def area(self):
        l,b = int(input("l: ")), int(input("b: "))
        print(l*b)

    def perimeter(self):
        l, b = int(input("l: ")), int(input("b: "))
        print(2*(l+b))

class Triangle(Shape):
    def area(self):
        b,h = int(input("b: ")), int(input("h: "))
        print((1/2)*b*h)

    def perimeter(self):
        b, h = int(input("b: ")), int(input("h: "))
        print(b*h)

c1 = Circle()
c1.area()
c1.perimeter()
# r1 = Rectangle()
# t1 = Triangle()
