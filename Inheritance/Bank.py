class Bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("deposited:",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdrawn:",amount)
        else:
            print("insufficient balance")
    def check_balance(self):
        print("Balance:", self.balance)
class User(Bank):
    def __init__(self,name,balance):
        super().__init__(balance)
        self.name=name
    def display(self):
        print("user name:",self.name)
# name = input("Enter name: ")
# balance = int(input("Enter initial balance: "))
u=User("x",1000)
# u = User(name, balance)
u.display()
u.deposit(5000)
u.withdraw(2000)
u.check_balance()

