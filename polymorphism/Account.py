class Account:
    def withdraw(self):
        print("Account withdrawal")

class SavingsAccount(Account):
    def withdraw(self):
        print("Savings account withdrawal")

class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self):
        super().withdraw()
        print("Premium savings withdrawal")


account = PremiumSavingsAccount()

account.withdraw()