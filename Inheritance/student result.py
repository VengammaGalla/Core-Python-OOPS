# class Student:
#     def __init(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("name:",self.name)
#         print("marks:",self.marks)
# class Result(Student):
#     def result(self):
#         if self.marks>=40:
#             print("result:pass")
#         else:
#             print("result:fail")
# name = input("Enter student name: ")
# marks = int(input("Enter marks: "))
# r = Result()
# r.display()
# r.result()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_marks(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
class Result(Student):
    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")
# name = input("Enter student name: ")
# marks = int(input("Enter marks: "))
# r = Result(name, marks)
r=Result("x",30)
r.display_marks()
r.result()