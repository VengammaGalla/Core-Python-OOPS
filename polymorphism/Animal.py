class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog says Woof")

class Cat(Animal):
    def make_sound(self):
        print("Cat says Meow")

class Cow(Animal):
    def make_sound(self):
        print("Cow says Moo")

animals = [Dog(), Cat(), Cow()]

for i in animals:
    i.make_sound()