class Product:

    def __init__(self, price, discount):
        if price < 0:
            price = 0

        if discount > 70:
            discount = 70

        self.__price = price
        self.__discount = discount

    def get_final_price(self):
        discount_amount = self.__price * self.__discount / 100
        final_price = self.__price - discount_amount
        return final_price

p = Product(1000, 20)

print(p.get_final_price())



class Product:
    def __init__(self,price,discount):
        if price<0:
            price=0
        if discount>70:
            discount=70

        self.__price=price
        self.__discount=discount

    def get_final_price(self):
        discount_amount=self.__price*self.__discount/100
        final_price=self.__price-discount_amount
        return final_price
p=Product(1000,50)
print(p.get_final_price())