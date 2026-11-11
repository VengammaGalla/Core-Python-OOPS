from abc import ABC, abstractmethod


# Product class
class Product:
    def __init__(self, product_id, name, price):
        if not self.validate_id(product_id):
            raise ValueError("Invalid product ID")
        self.product_id = product_id
        self.name = name
        self.price = price

    @staticmethod
    def validate_id(product_id):
        return isinstance(product_id, str) and product_id.isdigit()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    def __str__(self):
        return f"{self.name} - Rs.{self.price}"


# Abstract User class
class User(ABC):
    total_users = 0

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        User.total_users += 1

    @abstractmethod
    def get_role(self):
        pass

    @classmethod
    def get_total_users(cls):
        return User.total_users

    def check_password(self, password):
        return self.__password == password


# Seller
class Seller(User):
    def get_role(self):
        return "Seller"

    def checkout(self):
        print("Seller manages product sales")


# Rewards mixin
class RewardsMixin:
    def checkout(self):
        print("Rewards points applied")
        super().checkout()


# Cart class
class Cart:
    def __init__(self):
        self.__products = []

    def __add__(self, product):
        self.__products.append(product)
        return self

    def __sub__(self, product):
        if product in self.__products:
            self.__products.remove(product)
        return self

    def total(self):
        return sum(p.price for p in self.__products)

    def show(self):
        for product in self.__products:
            print(product)

    def __len__(self):
        return len(self.__products)


# Buyer
class Buyer(RewardsMixin, User):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.cart = Cart()

    def get_role(self):
        return "Buyer"

    def checkout(self):
        print("Buyer places an order")
        super().checkout()


# Order class
class Order:
    def __init__(self, buyer):
        self.buyer = buyer
        self.amount = buyer.cart.total()

    def __str__(self):
        return (
            f"Order for {self.buyer.name}: "
            f"Rs.{self.amount}"
        )


# Create products
laptop = Product("101", "Laptop", 50000)
mouse = Product("102", "Mouse", 500)

# Create users
seller = Seller("Ravi", "seller123")
buyer = Buyer("Sita", "buyer123")

# Add products to cart
buyer.cart = buyer.cart + laptop
buyer.cart = buyer.cart + mouse

print("Cart items:")
buyer.cart.show()

print("Total:", buyer.cart.total())
print("Role:", buyer.get_role())

buyer.checkout()

order = Order(buyer)
print(order)

print("Total users:", User.get_total_users())
print("MRO:", Buyer.mro())