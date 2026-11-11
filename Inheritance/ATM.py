class SBI:
    def __init__(self,name,accno,pin):
        self.name=name
        self.accno=accno
        self.pin=pin
        self.balance=0
        self.Transaction=[]

    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
            print(f"{amount} deposited")
            self.Transaction.append(f"{amount} deposited")
        else:
            print("insufficient amount")

    def check_balance(self):
        pin=int(input("enter the pin:"))
        if pin==self.pin:
            print(f"your current balance:{self.balance}")
        else:
            print("invalid pin")

class UnionBank:
    def __init(self,name,accno,pin):
        self.name = name
        self.accno = accno
        self.pin = pin
        self.balance = 0
        self.Transaction = []

    def withdraw(self,amount):
        pin=int(input("enter the pin:"))
        if pin==self.pin:
            if 0<=amount<=self.balance:
                self.balance-=amount
                print(f"your {amount}rs is withdrawn successfully")
                print(f"remaining balance:{self.balance}")
                self.Transaction.append(f"{amount} withdrawn")
            else:
                print("insufficient balance")
        else:
            print("invalid pin")

    def mini_statement(self):
        pin=int(input("enter the pin:"))
        if pin == self.pin:
            for i,j in enumerate(self.Transaction):
                print(f"{i}.{j}")
        else:
            print("invalid pin")

class ATM(SBI,UnionBank):
    def menu(self):
        print("1. deposit 2.withdraw 3.check_balance 4.mini_statement")
        self.d={1:self.deposit , 2:self.withdraw , 3:self.check_balance , 4:self.mini_statement}

    def transaction(self):
        self.menu()
        ch=int(input("enter your choice:"))
        if ch in self.d:
            if ch==1 or ch==2:
                a=int(input("enter the amount:"))
                self.d[ch](a)
            else:
                self.d[ch]()
        else:
            print("wrong choice")

a1=ATM("x",11237486,223344)
a1.transaction()
a1.transaction()
a1.transaction()
a1.transaction()
a1.transaction()



