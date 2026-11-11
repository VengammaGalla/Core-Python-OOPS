from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class UPIPayment(PaymentGateway):
    def authenticate(self):
        print("Authentication successful in UPI")

    def pay(self, amount):
        print(f"{amount} paid using UPI")

    def refund(self, amount):
        print(f"{amount} refunded to ur UPI account")

class CardPayment(PaymentGateway):
    def authenticate(self):
        print("Authentication successful in Card")

    def pay(self, amount):
        print(f"{amount} paid using Card")

    def refund(self, amount):
        print(f"{amount} refunded to ur card")

class NetBankingPayment(PaymentGateway):
    def authenticate(self):
        print("Authentication successful from ur Bank")

    def pay(self, amount):
        print(f"{amount} paid to Net account")

    def refund(self, amount):
        print(f"{amount} refunded to ur account")



l = [UPIPayment(), CardPayment(), NetBankingPayment()]
for i in l:
    i.authenticate()
    i.pay(1000)
    i.refund(100)