class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
class Manager(Employee):
    def bonus(self):
        bonus_amount=self.salary*0.10
        total_salary=self.salary+bonus_amount
        print("bonus:",bonus_amount)
        print("total salary:",total_salary)
name = input("Enter employee name: ")
salary = int(input("Enter salary: "))
m = Manager(name, salary)
m.display()
m.bonus()