class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("insufficient amount")
    def __str__(self):
        return "Account Holder: " + self.account_holder + ", Balance: " + str(self.balance)
    def __add__(self,other):
        return self.balance+other.balance
    def __sub__(self,other):
        return self.balance-other.balance
    def __eq__(self,other):
        return self.balance == other.balance
    def __lt__(self,other):
        return self.balance < other.balance
    def __getattribute__(self,name):
        print("accessing attribute",name)
        return object.__getattribute__(self,name)
    def __setattr__(self,name,value):
        if name=="balance" and value<0:
            print("negative balance is not allowed")
        else:
            object.__setattr__(self,name,value)

a1 = BankAccount("Venni", 10000)
a2 = BankAccount("Ravi", 7000)
print(a1)
print(a2)
a1.deposit(2000)
print(a1)
a2.withdraw(1000)
print(a2)
print(a1+a2)
print(a1-a2)
a1.balance = -500