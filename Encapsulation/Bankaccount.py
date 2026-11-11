class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Amount deposited")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Amount withdrawn")
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance


account = BankAccount("12345", 10000)

account.deposit(2000)
account.withdraw(3000)

print("Balance:", account.get_balance())

# Direct modification
account.__balance = 50000

print("Balance:", account.get_balance())