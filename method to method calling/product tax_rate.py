class Product:
    tax_rate=0
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        return self.base_price+(self.base_price*Product.tax_rate/100)
    @classmethod
    def change_tax_rate(cls,new_rate):
        cls.tax_rate=new_rate
    @staticmethod
    def is_valid_price(price):
        return price>=0 and price<=100
    def display(self):
        print("Name:",self.name)
        print("base Price:",self.base_price)
        print("tax rate:",self.tax_rate)
        print("final price:",self.final_price())
p1=Product("mobile",10000)
p1.display()
p1.change_tax_rate(1)
p1.display()
print(p1.final_price())
