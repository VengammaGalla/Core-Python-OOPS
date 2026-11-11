class Flipkart:
    usernames = {}

    def __init__(self, name, username, age, gender, psd):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = psd
        self.cart = []
        self.wishlist = []
        self.orders = []
        self.logged = False
        Flipkart.usernames[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")
        while True:
            username = input("Enter your username: ")
            if username in Flipkart.usernames.keys():
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

    def add_to_cart(self, product):
        if self.logged:
            if product not in self.cart:
                self.cart.append(product)
                print(product.name, "added to cart")
            else:
                print("Product already in cart")
        else:
            print("Not logged in")

    def remove_from_cart(self, product):
        if self.logged:
            if product in self.cart:
                self.cart.remove(product)
                print(product.name, "removed from cart")
            else:
                print("Product not found in cart")
        else:
            print("Not logged in")

    def add_to_wishlist(self, product):
        if self.logged:
            if product not in self.wishlist:
                self.wishlist.append(product)
                print(product.name, "added to wishlist")
            else:
                print("Product already in wishlist")
        else:
            print("Not logged in")

    def remove_from_wishlist(self, product):
        if self.logged:
            if product in self.wishlist:
                self.wishlist.remove(product)
                print(product.name, "removed from wishlist")
            else:
                print("Product not found in wishlist")
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

    def view_wishlist(self):
        if self.logged:
            if len(self.wishlist) == 0:
                print("Wishlist is empty")
            else:
                print("Your Wishlist")

                for i, j in enumerate(self.wishlist):
                    print(f"{i} : {j.name} - ₹{j.price}")
        else:
            print("Not logged in")

    def place_order(self):
        if self.logged:
            if len(self.cart) == 0:
                print("Cart is empty")
            else:
                total = 0

                for product in self.cart:
                    total += product.price

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

                    for product in order:
                        print(product.name, "- ₹", product.price)
        else:
            print("Not logged in")

    def profile(self):
        print(f"{self.name}'s Profile")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Cart Items : {len(self.cart)}")
        print(f"Wishlist Items : {len(self.wishlist)}")
        print(f"Orders : {len(self.orders)}")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ₹{self.price}")


# Products

p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 20000)
p3 = Product("Headphones", 2000)
p4 = Product("Smart Watch", 3000)
p5 = Product("Keyboard", 1500)

# Display products

print("Available Products")

p1.display()
p2.display()
p3.display()
p4.display()
p5.display()
f1 = Flipkart.signup()
f2 = Flipkart.signup()

# Login

f1.login()

# Add products to cart

f1.add_to_cart(p1)
f1.add_to_cart(p3)

# Add product to wishlist

f1.add_to_wishlist(p4)
f1.add_to_wishlist(p5)

# View cart

f1.view_cart()

# View wishlist

f1.view_wishlist()

# Remove from cart

f1.remove_from_cart(p3)

# View cart

f1.view_cart()

# Place order

f1.place_order()

# View orders

f1.view_orders()

# Profile

f1.profile()

# Logout

f1.logout()