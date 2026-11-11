class Swiggy:
    usernames = {}

    def __init__(self, name, username, age, gender, psd):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = psd
        self.cart = []
        self.orders = []
        self.logged = False
        Swiggy.usernames[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")
        while True:
            username = input("Enter your username: ")
            if username in Swiggy.usernames.keys():
                print("Username already registered try another one")
                continue
            break

        psd = input("Enter Your Password: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender(Male/Female): ")
        return cls(name, username, age, gender, psd)

    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            user = input("Enter your username: ")
            password = input("Enter your password: ")
            if user == self.username and password == self.password:
                self.logged = True
                print("Logged in Successfully")
            else:
                print("Invalid Credentials")

    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out successfully")
        else:
            print("Already logged out")

    def add_to_cart(self, food):
        if self.logged:
            self.cart.append(food)
            print(food.name, "added to cart")
        else:
            print("Not logged in")

    def remove_from_cart(self, food):
        if self.logged:
            if food in self.cart:
                self.cart.remove(food)
                print(food.name, "removed from cart")
            else:
                print("Food not found in cart")
        else:
            print("Not logged in")

    def view_cart(self):
        if self.logged:
            if len(self.cart) == 0:
                print("Cart is empty")
            else:
                print("Your Cart")
                total = 0
                for i, j in enumerate(self.cart):
                    print(f"{i} : {j.name} - ₹{j.price}")
                    total += j.price
                print("Total : ₹", total)
        else:
            print("Not logged in")

    def place_order(self):
        if self.logged:
            if len(self.cart) == 0:
                print("Cart is empty")
            else:
                total = 0
                for food in self.cart:
                    total += food.price
                self.orders.append(self.cart.copy())
                self.cart.clear()
                print("Order placed successfully")
                print("Total Amount : ₹", total)
        else:
            print("Not logged in")

    def view_orders(self):
        if self.logged:
            if len(self.orders) == 0:
                print("No orders found")
            else:
                print("Your Orders")

                for i, order in enumerate(self.orders):
                    print("Order", i + 1)

                    for food in order:
                        print(food.name, "- ₹", food.price)
        else:
            print("Not logged in")

    def profile(self):
        print(f"{self.name}'s Profile")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Cart Items : {len(self.cart)}")
        print(f"Orders : {len(self.orders)}")


class Food:
    def __init__(self, name, price, restaurant):
        self.name = name
        self.price = price
        self.restaurant = restaurant

    def display(self):
        print(f"{self.name} - ₹{self.price} - {self.restaurant}")


# Food items

f1 = Food("Chicken Biryani", 250, "Paradise")
f2 = Food("Chicken Fried Rice", 180, "Bawarchi")
f3 = Food("Pizza", 300, "Dominos")
f4 = Food("Burger", 150, "Burger King")
f5 = Food("Ice Cream", 100, "Cream Stone")


# Display food

print("Available Food")

f1.display()
f2.display()
f3.display()
f4.display()
f5.display()
# Creating users
s1 = Swiggy.signup()
s2 = Swiggy.signup()
# Login
s1.login()
# Add food to cart
s1.add_to_cart(f1)
s1.add_to_cart(f3)
s1.add_to_cart(f5)
# View cart
s1.view_cart()
# Remove food
s1.remove_from_cart(f5)
# View cart again
s1.view_cart()
# Place order
s1.place_order()
# View orders
s1.view_orders()
# Profile
s1.profile()
# Logout
s1.logout()