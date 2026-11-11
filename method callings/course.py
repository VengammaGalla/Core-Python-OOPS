class Course:
    total_students=0
    def __init__(self,student_name):
        self.name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print("Total students:",cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
c1=Course("x")
print(c1.is_eligible(20))
c1.enroll()
c2=Course("y")
print(c2.is_eligible(13))
c2.enroll()
Course.show_total()



