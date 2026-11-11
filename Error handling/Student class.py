class Student:
    def set_marks(self, marks):
        self.marks = marks
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

s = Student()

try:
    s.set_marks(105)
    print(s.marks)
except ValueError as e:
    print("Error:", e)