class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage = mileage
    def display_specs(self):
        print(f"Mileage: {self.mileage}")
        print(f"Wheels: {self.wheels}")
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
        print(f"wheels: {cls.wheels}")
c1=Car(100)
c2=Car(200)
c1.display_specs()
c2.display_specs()
Car.change_wheels(8)


