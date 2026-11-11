class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            print("passed")
        else:
            print("failed")
    @classmethod
    def update_passing_marks(cls,new_marks):
        Student.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=90:
            return "A"
        elif marks>=75:
            return "B"
        elif marks>=40:
            return "C"
        else:
            return "f"
s1=Student("Venni",80)
s1.result()
s1.grade_category(s1.marks)
s1.update_passing_marks(50)
s1.result()
print(f"Student name: {s1.name} and grade is {Student.grade_category(s1.marks)}")
print(Student.grade_category(s1.marks))