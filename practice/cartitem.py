# Create a class CartItem with:
# 	attributes: item_name, price, quantity
# 	method: final_amount()
# Implement:
# 	__str__()
# 	__add__() → add final amounts of two cart items
# 	__mod__() → find remainder after applying a discount value
# 	__lt__() → compare item total amount
# 	__ge__() → compare quantity
# 	__getattribute__() → display which attribute is being accessed
# 	__setattr__() → quantity cannot be less than 1
class CartItem:
    def __init__(self,item_name,price,quantity):
        self.item_name=item_name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return "Item: " + self.item_name + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity)
    def final_amount(self):
        return self.price * self.quantity
    def __add__(self,other):
        return self.final_amount()+other.final_amount()
    def __mod__(self,discount):
        return self.final_amount()%discount
    def __lt__(self,other):
        return self.final_amount()<other.final_amount()
    def __ge__(self,other):
        return self.quantity>=other.quantity
    def __getattribute__(self,name):
        print(f"{name} is accessed")
        return super().__getattribute__(name)
    def __setattr__(self,name,value):
        if name=="quantity":
            if value<1:
                print("Quantity cannot be less than 1")
                return
        object.__setattr__(self,name,value)


c1=CartItem("Laptop",50000,2)
c2=CartItem("Mouse",1000,3)

print(c1)

print("Final Amount:",c1.final_amount())

print("Total of two items:",c1+c2)

print("Remainder after discount:",c1%1000)

print("c1 total < c2 total:",c1<c2)

print("c1 quantity >= c2 quantity:",c1>=c2)

c1.quantity=5
print(c1)

c1.quantity=0

