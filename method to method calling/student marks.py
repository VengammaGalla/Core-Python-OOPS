class Student:
    total=0
    curve=0
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.total+=1
    def result(self):
        if self.marks>Student.passing_marks:
            return "pass"
        else:
            return "fail"
    @classmethod
    def curve_marks(cls, Student, percentage):
        for Student in Student:
            Student.marks += Student.marks * percentage / 100
    @staticmethod
    def grade(marks):
        if marks>90:
            return "A"
        elif marks>=70:
            return "B"
        elif marks>=40:
            return "C"
        else:
            return "f"
    def display(self):
        print(f"name:", self.name)
        print(f"marks:",self.marks)
        print(f"total:",self.total)
        print(f"grade:",self.grade(self.marks))
s1=Student("venni",90)
s1.display()
s2=Student.grade(90)
s3=Student("vvvv",30)
s3.display()
# for Student in Student:
#     Student.display()
# Student.curve_marks(Student,10)
print("Total Students =", Student.total)

