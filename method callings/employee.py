class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("venni")
print(e1.name,e1.company_name)
Employee.change_company("Infosys")
print(e1.company_name)
