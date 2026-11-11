class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        print("Remaining balance:", self.balance)

b = BankAccount(5000)

try:
    b.withdraw(6000)
except ValueError as e:
    print("Error:", e)