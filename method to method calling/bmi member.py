class Member:
    bmi_limit = 25
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def check_bmi(self):
        bmi = self.weight / (self.height ** 2)
        print("Name:", self.name)
        print("BMI:", round(bmi, 2))

        if bmi <= Member.bmi_limit:
            print("Status: Fit")
        else:
            print("Status: Not Fit")
    @classmethod
    def update_limit(cls, new_limit):
        cls.bmi_limit = new_limit
    @staticmethod
    def valid(height, weight):
        if height > 0 and weight > 0:
            return "Valid Input"
        else:
            return "Invalid Input"
m1 = Member("Ravi", 1.70, 65)
m2 = Member("Sneha", 1.60, 75)

print("Before Updating BMI Limit")
m1.check_bmi()
m2.check_bmi()

# Updating BMI limit
Member.update_limit(23)

print("\nAfter Updating BMI Limit")
m1.check_bmi()
m2.check_bmi()

# Input validation
print("\nInput Validation")
print(Member.valid(1.70, 65))
print(Member.valid(-1.60, 75))