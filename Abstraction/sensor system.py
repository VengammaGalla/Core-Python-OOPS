from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def read_value(self):
        pass

    @abstractmethod
    def calibrate(self):
        pass

    def get_reading(self):
        self.calibrate()
        return self.read_value()


class TemperatureSensor(Sensor):

    def __init__(self):
        self.__raw_value = 30
        self.__calibration_factor = 1.1

    def read_value(self):
        return self.__raw_value * self.__calibration_factor

    def calibrate(self):
        print("Calibrating temperature sensor")


class PressureSensor(Sensor):

    def __init__(self):
        self.__raw_value = 100
        self.__calibration_factor = 1.2

    def read_value(self):
        return self.__raw_value * self.__calibration_factor

    def calibrate(self):
        print("Calibrating pressure sensor")


class HumiditySensor(Sensor):

    def __init__(self):
        self.__raw_value = 50
        self.__calibration_factor = 0.9

    def read_value(self):
        return self.__raw_value * self.__calibration_factor

    def calibrate(self):
        print("Calibrating humidity sensor")


temperature = TemperatureSensor()
pressure = PressureSensor()
humidity = HumiditySensor()

print("Temperature:", temperature.get_reading())
print("Pressure:", pressure.get_reading())
print("Humidity:", humidity.get_reading())