class Restaurant:
    def menu(self, item):
        if item == "pizza":
            return 200
        elif item == "burger":
            return 100
        elif item == "biryani":
            return 250
        elif item == "kfc":
            return 150
        else:
            return 0

class FoodCourt(Restaurant):

    def display_menu(self):
        print("----- MENU -----")
        print("pizza - 200")
        print("burger - 100")
        print("biryani - 250")
        print("kfc - 150")

    def order(self):
        self.orders = []

        self.display_menu()

        while True:
            item = input("Enter food item: ").lower()

            price = self.menu(item)

            if price == 0:
                print("Invalid item")
            else:
                self.orders.append(price)
                print(item, "added -", price)

            choice = input("Do you want to order more? yes/no: ").lower()

            if choice == "no":
                break

        self.billing()

    def billing(self):
        total = sum(self.orders)
        packing = 20

        final_bill = total + packing

        print("\n----- BILL -----")
        print("Food total:", total)
        print("Packing charge:", packing)
        print("Total bill:", final_bill)


# class FoodCourt:
#
#     def order(self):
#         print("Food ordered")

class Customer(FoodCourt):
    pass

# c1 = Customer()
#
# c1.order()


c = Customer()
c.order()
c.billing()
# c.final_bill()