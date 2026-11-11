class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

class Rectangle:
    def draw(self):
        print("Drawing Rectangle")

class Car:
    def draw(self):
        print("Drawing Car")

def draw(shape):
    shape.draw()

draw(Circle())
draw(Square())
draw(Rectangle())
draw(Car())