class Employee:
    experience=5
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def check_promotion(self):
        if self.experience>=Employee.experience:
            return "eligible for promotion"
        else:
            return "not eligible"
    @classmethod
    def update_promotion(cls,years):
        Employee.experience=years
    @staticmethod
    def is_valid_department(dept):
        valid_departments = ["HR", "Tech", "Admin"]

        if dept in valid_departments:
            return "Valid Department"
        else:
            return "Invalid Department"
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("department:",self.department)
        print("experience:",self.experience,"years")
        print("promotion:",self.check_promotion())
e1=Employee("James",20000,"HR")
e1.display()
Employee.update_promotion(10)
e1.display()
print(Employee.is_valid_department("HR"))
print(Employee.is_valid_department("Tech"))
print(Employee.is_valid_department("Sales"))
