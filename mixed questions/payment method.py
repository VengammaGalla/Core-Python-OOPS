from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    def __init__(self, balance):
        self._balance = balance       # encapsulated balance

    @property
    def available_funds(self):
        return self._balance

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    def __add__(self, other):
        return SplitPayment(self, other)


class CardPayment(PaymentMethod):

    def validate(self):
        return True

    def pay(self, amount):
        if self.validate() and self._balance >= amount:
            self._balance -= amount
            print("Paid using Card:", amount)
            return True
        return False


class WalletPayment(PaymentMethod):

    def validate(self):
        return True

    def pay(self, amount):
        if self.validate() and self._balance >= amount:
            self._balance -= amount
            print("Paid using Wallet:", amount)
            return True
        return False

class UPIPayment(PaymentMethod):

    def validate(self):
        return True

    def pay(self, amount):
        if self.validate() and self._balance >= amount:
            self._balance -= amount
            print("Paid using UPI:", amount)
            return True
        return False

class SplitPayment(PaymentMethod):

    def __init__(self, payment1, payment2):
        self.payment1 = payment1
        self.payment2 = payment2

    def validate(self):
        return True

    def pay(self, amount):
        half = amount / 2

        if self.payment1.available_funds >= half and \
           self.payment2.available_funds >= half:

            self.payment1.pay(half)
            self.payment2.pay(half)

            print("Split payment completed")
            return True

        print("Insufficient balance")
        return False

# Creating payment methods
card = CardPayment(5000)
wallet = WalletPayment(3000)
upi = UPIPayment(2000)

# Polymorphism
payments = [card, wallet, upi]

for payment in payments:
    payment.pay(500)

# Operator overloading
split = card + wallet

split.pay(1000)

print("Card balance:", card.available_funds)
print("Wallet balance:", wallet.available_funds)