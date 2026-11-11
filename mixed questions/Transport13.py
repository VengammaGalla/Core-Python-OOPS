from abc import ABC, abstractmethod

class Transport(ABC):
    tax_rate = 0.05

    def __init__(self, distance):
        if not self.valid_distance(distance):
            raise ValueError("Invalid distance")

        self.distance = distance
        self.__fare = 0

    @staticmethod
    def valid_distance(distance):
        return distance > 0

    @abstractmethod
    def calculate_fare(self):
        pass

    def get_total_fare(self):
        self.__fare = self.calculate_fare()
        return self.__fare * (1 + Transport.tax_rate)

    @classmethod
    def update_tax(cls, new_rate):
        if new_rate < 0:
            raise ValueError("Tax cannot be negative")
        Transport.tax_rate = new_rate


class Taxi(Transport):
    def calculate_fare(self):
        return self.distance * 20


class Bus(Transport):
    def calculate_fare(self):
        return self.distance * 5


class Train(Transport):
    def calculate_fare(self):
        return self.distance * 3


for vehicle in [Taxi(10), Bus(10), Train(10)]:
    print(type(vehicle).__name__, vehicle.get_total_fare())

Transport.update_tax(0.10)
print("Updated taxi fare:", Taxi(10).get_total_fare())