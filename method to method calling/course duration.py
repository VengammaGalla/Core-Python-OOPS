class Course:
    total=0
    duration=30
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
        self.enroll_students=[]
        self.total+=1
    def enroll(self,student):
        self.enroll_students.append(student)
    def display(self):
        print("title:",self.title)
        print("duration:",self.duration)
        print("students:",self.enroll_students)
        print()
    @classmethod
    def update(cls,nd):
        cls.duration=nd
    @staticmethod
    def is_valid_duration(duration):
        return duration > 0
c1 = Course("Python", 60)
c2 = Course("Java", 45)

# Enrolling students
c1.enroll("Rahul")
c1.enroll("Anitha")

c2.enroll("Kiran")

# Display details
c1.display()
c2.display()

# Total courses
print("Total Courses:", Course.total)

# Update minimum duration
Course.update(40)
print("Updated Minimum Duration:", Course.duration)

# Check durations
print(Course.is_valid_duration(50))
print(Course.is_valid_duration(-10))
print(Course.is_valid_duration(700))
