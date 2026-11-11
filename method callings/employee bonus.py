class Employee:
    bonus_rate=0.1
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def final_salary(self):
        k=self.base_salary+(self.base_salary*self.bonus_rate)
        print(f"Name: {self.name}")
        print(f"final salary: {k}")
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
e1=Employee("venni",1000)
e2=Employee("james",10000)
e1.final_salary()
e2.final_salary()
e1.update_bonus(2.1)
e1.final_salary()
