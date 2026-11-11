from abc import ABC, abstractmethod

class MenuItem(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Pizza(MenuItem):
    def get_price(self):
        return 250


class Burger(MenuItem):
    def get_price(self):
        return 120


class Drink(MenuItem):
    def get_price(self):
        return 50


class Order:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def total(self):
        return sum(item.get_price() for item in self.__items)


order = Order()
order.add_item(Pizza())
order.add_item(Burger())
order.add_item(Drink())

print("Total bill:", order.total())