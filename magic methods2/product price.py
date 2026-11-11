class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_price(self):
        return self.price*self.quantity
    def __str__(self):
        return "Name:"+self.name+",price:"+str(self.price)+",Quantity:"+str(self.quantity)
    def __add__(self,other):
        return self.total_price()+other.total_price()
    def __mul__(self,number):
        return self.price*number
    def __gt__(self,other):
        return self.total_price()>other.total_price()
    def __eq__(self,other):
        return self.price==other.price
    def __getattr__(self,name):
        return "attribute not found"
    def __setattr__(self,name,value):
        if name=="price"and value<0:
            print("price cannot be less than 0")
        else:
            object.__setattr__(self,name,value)
p1 = Product("Laptop", 50000, 2)
p2 = Product("Mobile", 20000, 3)
print(p1)
print(p2)

# Total price
print("P1 Total Price:", p1.total_price())
print("P2 Total Price:", p2.total_price())
print("Addition of total prices:", p1 + p2)

print("Price multiplied by 3:", p1 * 3)

print("P1 has greater total value:", p1 > p2)

print("Same price:", p1 == p2)

# Missing attribute
print(p1.brand)

# Negative price
p1.price = -100