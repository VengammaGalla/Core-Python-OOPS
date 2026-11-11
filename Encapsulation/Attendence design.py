class Student:

    def __init__(self):
        self.attendance = []

    def mark_attendance(self, name):
        self.attendance.append(name)

s = Student()

s.mark_attendance("Vennela")

print(s.attendance)

s.attendance.append("Rahul")

print(s.attendance)



#CORRECT DESIGN

class Student:

    def __init__(self):
        self.__attendance = []

    def mark_attendance(self, name):
        self.__attendance.append(name)

    def get_attendance(self):
        return self.__attendance.copy()


s = Student()

s.mark_attendance("Vennela")
s.mark_attendance("Rahul")

print(s.get_attendance())