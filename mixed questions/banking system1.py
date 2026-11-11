from abc import ABC, abstractmethod

class Account(ABC):
    # Bank-wide interest policies
    savings_rate = 4
    current_rate = 2
    fixed_rate = 7

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance       # private variable

    # Property to access balance
    @property
    def balance(self):
        return self.__balance

    # Controlled way to change balance
    @balance.setter
    def balance(self, amount):
        if self.validate_amount(amount):
            self.__balance = amount

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if self.validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Invalid withdrawal")

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @classmethod
    def update_interest_policy(cls, savings, current, fixed):
        cls.savings_rate = savings
        cls.current_rate = current
        cls.fixed_rate = fixed
        print("Interest policies updated")

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):

    def calculate_interest(self):
        return self.balance * Account.savings_rate / 100


class CurrentAccount(Account):

    def calculate_interest(self):
        return self.balance * Account.current_rate / 100


class FixedDepositAccount(Account):

    def calculate_interest(self):
        return self.balance * Account.fixed_rate / 100

# Creating different account types
savings = SavingsAccount("S101", 50000)
current = CurrentAccount("C101", 80000)
fixed = FixedDepositAccount("F101", 100000)

# Deposit and withdrawal
savings.deposit(5000)
current.withdraw(10000)

print()

# Polymorphism
accounts = [savings, current, fixed]

for account in accounts:
    print("Account:", account.account_no)
    print("Balance:", account.balance)
    print("Interest:", account.calculate_interest())
    print()

# Preventing direct access to private balance
print("Direct balance access:")

try:
    print(savings.__balance)
except AttributeError:
    print("Cannot access balance directly")

# Updating bank-wide interest policies
Account.update_interest_policy(5, 3, 8)

print()

# Interest after policy update
for account in accounts:
    print(account.account_no, "Interest:", account.calculate_interest())