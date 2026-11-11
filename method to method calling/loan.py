class Loan:
    intrest_rate=10
    def __init__(self,borrower_name,principal):
        self.borrower_name=borrower_name
        self.principal=principal
    def total_payable(self):
        return self.principal+(self.principal*Loan.intrest_rate/100)
    @classmethod
    def update_intrest_rate(cls,new_rate):
        cls.intrest_rate=new_rate
    @staticmethod
    def check_eligibility(salary):
        if salary > 10000:
            return "Eligible"
        else:
            return "Not Eligible"
    def display(self):
        # print("borrower Name":,self.borrower_name)
        print("Principal:",self.principal)
        print("Total payable:",self.total_payable())
l1=Loan("venni",10000)
l1.display()

