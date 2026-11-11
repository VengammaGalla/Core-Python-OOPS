class Grocery:
    def rice(self):
        return 60
    def sugar(self):
        return 50
    def oil(self):
        return 120

class Dmart(Grocery):

    def items(self):
        print("----- DMART -----")
        print("1. Rice - ₹60")
        print("2. Sugar - ₹50")
        print("3. Oil - ₹120")

    def shopping(self):
        self.total = 0

        self.items()

        while True:
            choice = int(input("Enter item number: "))
            quantity = int(input("Enter quantity: "))

            if choice == 1:
                self.total = self.total + self.rice() * quantity
            elif choice == 2:
                self.total = self.total + self.sugar() * quantity
            elif choice == 3:
                self.total = self.total + self.oil() * quantity
            else:
                print("Invalid item")

            more = input("Do you want to buy another item? yes/no: ").lower()

            if more == "no":
                break

        self.billing()

    def billing(self):
        print("Bill amount:", self.total)

        gst = self.total * 5 / 100
        amount = self.total + gst

        if self.total > 2000:
            discount = amount * 10 / 100
            amount = amount - discount
            print("Discount:", discount)

        print("GST:", gst)
        print("Final Bill:", amount)


class RelianceSmart(Grocery):

    def items(self):
        print("----- RELIANCE SMART -----")
        print("1. Rice - ₹60")
        print("2. Sugar - ₹50")
        print("3. Oil - ₹120")

    def shopping(self):
        self.total = 0

        self.items()

        while True:
            choice = int(input("Enter item number: "))
            quantity = int(input("Enter quantity: "))

            if choice == 1:
                self.total = self.total + self.rice() * quantity
            elif choice == 2:
                self.total = self.total + self.sugar() * quantity
            elif choice == 3:
                self.total = self.total + self.oil() * quantity
            else:
                print("Invalid item")

            more = input("Do you want to buy another item? yes/no: ").lower()

            if more == "no":
                break

        self.billing()

    def billing(self):
        print("Bill amount:", self.total)

        gst = self.total * 5 / 100
        amount = self.total + gst

        if self.total > 2500:
            discount = amount * 15 / 100
            amount = amount - discount
            print("Discount:", discount)

        print("GST:", gst)
        print("Final Bill:", amount)


# Driver Code

print("1. Dmart")
print("2. Reliance Smart")

choice = int(input("Choose supermarket: "))

if choice == 1:
    d = Dmart()
    d.shopping()

elif choice == 2:
    r = RelianceSmart()
    r.shopping()

else:
    print("Invalid choice")