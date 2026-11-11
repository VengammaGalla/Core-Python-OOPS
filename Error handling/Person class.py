class Person:
    def __init__(self, age):
        self.age = age
        if age < 0:
            raise ValueError("Age cannot be negative")

try:
    p = Person(-5)
    print(p.age)
except ValueError as e:
    print("Error:", e)