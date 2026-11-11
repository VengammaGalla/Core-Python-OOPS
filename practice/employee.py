# Create a class Employee with:
# 	attributes: name, salary
# 	method: annual_salary()
# Implement:
# 	__str__()
# 	__add__() → add salaries of two employees
# 	__mul__() → calculate salary after multiplying by months
# 	__ne__() → check if salaries are not equal
# 	__le__() → check if one salary is less than or equal to another
# 	__getattribute__() → log every attribute access
# 	__setattr__() → salary cannot be below 10000
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return "Name: " + self.name + ", Salary: " + str(self.salary)
    def annual_salary(self):
        return self.salary * 12
    def __add__(self,other):
        return self.salary+other.salary
    def __mul__(self,months):
        return self.salary*months
    def __ne__(self,other):
        return self.salary!=other.salary
    def __le__(self,other):
        return self.salary<=other.salary
    def __getattribute__(self,name):
        print(f"{name} is accessing")
        return super().__getattribute__(name)
    def __setattr__(self,name,value):
        if name=="salary":
            if value<10000:
                print("Salary cannot be below 10000")
                return
        object.__setattr__(self,name,value)

e1=Employee("Vennela",25000)
e2=Employee("Anu",30000)

print(e1)
print("Annual Salary:",e1.annual_salary())

print("Total Salary:",e1+e2)

print("Salary for 6 months:",e1*6)

print("Salaries are not equal:",e1!=e2)

print("e1 salary <= e2 salary:",e1<=e2)

e1.salary=35000
print(e1)

e1.salary=5000
