class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.valid_amount(amount):
            self.balance=self.balance+amount
            print(f"total amount is {self.balance}")
        else:
            print("Invalid amount")
    @classmethod
    def change_bank_name(cls,new_value):
        BankAccount.bank_name=new_value
        return(f"Bank name has been changed to {new_value}")
    @staticmethod
    def valid_amount(amount):
        return amount>0
b1=BankAccount("venni",100)
print(b1.balance)
b1.deposit(300)
print(BankAccount.bank_name)
print(b1.change_bank_name("axis"))