class ShoppingCart:

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def get_items(self):
        return self.__items.copy()

cart = ShoppingCart()

cart.add_item("Apple")
cart.add_item("Milk")

print(cart.get_items())

items = cart.get_items()
items.append("Laptop")

print(items)
print(cart.get_items())