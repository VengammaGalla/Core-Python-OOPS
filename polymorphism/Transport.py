class Transport:
    def move(self):
        print("Transport is moving")

class Bus(Transport):
    def move(self):
        super().move()
        print("Bus is carrying passengers")

class Bike(Transport):
    def move(self):
        super().move()
        print("Bike is moving on two wheels")


b = Bus()
b.move()

print()

bike = Bike()
bike.move()