from abc import ABC, abstractmethod
class VehicleControl(ABC):

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def steer(self):
        pass

class CarControl(VehicleControl):

    def accelerate(self):
        print("Car is accelerating")

    def brake(self):
        print("Car is braking")

    def steer(self):
        print("Car is steering")

class BikeControl(VehicleControl):

    def accelerate(self):
        print("Bike is accelerating")

    def brake(self):
        print("Bike is braking")

    def steer(self):
        print("Bike is steering")


class TruckControl(VehicleControl):

    def accelerate(self):
        print("Truck is accelerating")

    def brake(self):
        print("Truck is braking")

    def steer(self):
        print("Truck is steering")


# Single interface
vehicles = [CarControl(), BikeControl(), TruckControl()]

for vehicle in vehicles:
    vehicle.accelerate()
    vehicle.brake()
    vehicle.steer()
    print()

from abc import ABC,abstractmethod
class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def steer(self):
        pass
class CarControl(VehicleControl):
    def accelerate(self):
        print("car is accelerating")
    def brake(self):
        print("car is braking")
    def steer(self):
        print("car is steering")
