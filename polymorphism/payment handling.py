class UPI:
    def pay(self):
        print("Payment through UPI")

class Card:
    def pay(self):
        print("Payment through Card")

class Cash:
    def pay(self):
        print("Payment through Cash")

def make_payment(payment):
    payment.pay()


make_payment(UPI())
make_payment(Card())
make_payment(Cash())