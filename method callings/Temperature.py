class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def show_conversion(self):
        fahrenheit = Temperature.to_fahrenheit(self.celsius)
        print("Celsius:", self.celsius)
        print("Fahrenheit:", fahrenheit)


# Creating object
t1 = Temperature(25)

# Display conversion
t1.show_conversion()