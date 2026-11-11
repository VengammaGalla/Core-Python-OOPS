class Vehicle:

    def calculate_fare(self, distance):
        return 0

class Car(Vehicle):

    def calculate_fare(self, distance):
        return distance * 15

class Bike(Vehicle):

    def calculate_fare(self, distance):
        return distance * 10

class Auto(Vehicle):

    def calculate_fare(self, distance):
        return distance * 12

class Driver:

    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

class Ride:

    def __init__(self, driver, distance):
        self.driver = driver
        self.__distance = distance       # private

    def calculate_fare(self):
        return self.driver.vehicle.calculate_fare(self.__distance)

    def __str__(self):
        return "Driver: " + self.driver.name + \
               ", Vehicle: " + self.driver.vehicle.__class__.__name__ + \
               ", Fare: " + str(self.calculate_fare())

# Creating vehicles
car = Car()
bike = Bike()
auto = Auto()

# Creating drivers
d1 = Driver("Ravi", car)
d2 = Driver("Sita", bike)
d3 = Driver("Rahul", auto)

# Creating rides
ride1 = Ride(d1, 10)
ride2 = Ride(d2, 10)
ride3 = Ride(d3, 10)

print(ride1)
print(ride2)
print(ride3)