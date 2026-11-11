class Course:

    def fee(self, course):
        if course == "python":
            return 5000
        elif course == "java":
            return 6000
        elif course == "web":
            return 7000
        else:
            return 0

class Academy(Course):

    def courses(self):
        print("Available Courses")
        print("python - 5000")
        print("java - 6000")
        print("web - 7000")

    def enroll(self):
        self.total = 0

        self.courses()

        while True:
            course = input("Enter course name: ").lower()

            price = self.fee(course)

            if price == 0:
                print("Invalid course")
            else:
                self.total = self.total + price
                print("Course enrolled:", price)

            choice = input("Do you want to enroll another course? yes/no: ").lower()

            if choice == "no":
                break

        self.billing()

    def billing(self):
        print("Course fee:", self.total)
        print("Registration fee: 100")
        print("Total fee:", self.total + 100)


class Student(Academy):
    pass


s = Student()
s.enroll()