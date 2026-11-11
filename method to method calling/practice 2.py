class product:
    tax_rate=0
    def __init__(self, name,base_price,):
        self.name = name
        self.base_price =base_price
    def final_price(self):
        print(self.base_price + (self.base_price * product.tax_rate / 100))
    @classmethod
    def change_tax(cls,nt):
        cls.tax_rate=nt
    @staticmethod
    def check(price):
        if price >0:
            return "valid"
        else:
            return "invalid"
    def display(self):
        print(f"name:",self.name)
        print(f"base_price:",self.base_price)
        print(f"tax_rate:",self.tax_rate)
p1=product("A",100,)
p1.display()
product.change_tax(100)
p1.display()


