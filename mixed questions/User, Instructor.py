class User:
    def __init__(self, name):
        self.name = name

    def submit_work(self):
        print("User submits work")

    def grade_work(self):
        print("User grades work")


class Instructor(User):
    def grade_work(self):
        print("Instructor grades assignments")


class Student(User):
    def submit_work(self):
        print("Student submits assignment")


class TeachingAssistant(Student, Instructor):
    def __init__(self, name):
        super().__init__(name)
        self.__courses = ["Python", "SQL"]

    def submit_work(self):
        print("Teaching assistant submits work")

    def grade_work(self):
        print("Teaching assistant grades work")


ta = TeachingAssistant("Ravi")

ta.submit_work()
ta.grade_work()

print(TeachingAssistant.mro())