class Student:

    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print("Marks updated")
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks

s = Student("Vennela")

s.set_marks(85)
print("Marks:", s.get_marks())

s.set_marks(150)
print("Marks:", s.get_marks())

# Trying to assign directly
s.__marks = 200

print("Marks:", s.get_marks())