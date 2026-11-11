class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        return self.marks >40

s1=Student("venni",100)
s2=Student("vennela",30)
print(s1.name,s1.marks)
print(s2.name,s2.marks)