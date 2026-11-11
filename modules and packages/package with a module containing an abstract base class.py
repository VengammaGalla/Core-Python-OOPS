from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# from vehicles.base import Vehicle
#
# class Car(Vehicle):
#     def start(self):
#         print("Car starts with a key")
#
# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts with a button")