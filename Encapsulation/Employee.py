class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        print("Salary access attempted")
        return self.__salary

    def update_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary updated")
        else:
            print("Salary cannot be decreased")

e = Employee(30000)

print(e.get_salary())

e.update_salary(40000)
print(e.get_salary())

e.update_salary(25000)
print(e.get_salary())