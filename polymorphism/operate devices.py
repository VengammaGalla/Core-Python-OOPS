class Car:
    def start(self):
        print("Car starts")

class Computer:
    def start(self):
        print("Computer starts")

class WashingMachine:
    def start(self):
        print("Washing machine starts")

def operate(device):
    device.start()

operate(Car())
operate(Computer())
operate(WashingMachine())

