class Student:

    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value >= 0 and value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")
s = Student(80)
print(s.marks)
s.marks = 90
print(s.marks)
s.marks = 150
print(s.marks)

#2. Forgetting the underscore prefix

class Student:

    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self.marks

#3. Setter without validation

class Student:

    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        self.__marks = value
s = Student(80)
s.marks = -500
print(s.marks)

#Better setter

@marks.setter
def marks(self, value):

    if value >= 0 and value <= 100:
        self.__marks = value
    else:
        print("Invalid marks")
s.marks = -500