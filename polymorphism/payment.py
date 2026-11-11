class Payment:
    def process(self, amount):
        print("Processing payment:", amount)


class CreditCardPayment(Payment):
    def process(self, amount, card_type):
        print("Processing", card_type, "payment:", amount)


p = CreditCardPayment()

p.process(100, "Visa")