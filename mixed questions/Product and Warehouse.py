class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.__quantity = quantity

    def __repr__(self):
        return f"{self.name}: {self.__quantity} units"


class Warehouse:
    total_warehouses = 0

    def __init__(self, products=None):
        self.products = {}
        Warehouse.total_warehouses += 1

        if products:
            for product in products:
                self.products[product.name] = product

    def __add__(self, other):
        merged = Warehouse()
        merged.products = self.products.copy()

        for name, product in other.products.items():
            if name in merged.products:
                old = merged.products[name]
                merged.products[name] = Product(
                    name, old._Product__price,
                    old._Product__quantity + product._Product__quantity
                )
            else:
                merged.products[name] = product

        return merged

    def __len__(self):
        return len(self.products)

    def __contains__(self, name):
        return name in self.products

    @classmethod
    def get_total(cls):
        return cls.total_warehouses


w1 = Warehouse([Product("Laptop", 50000, 2)])
w2 = Warehouse([Product("Phone", 20000, 3)])

w3 = w1 + w2

print(len(w3))
print("Laptop" in w3)
print(Warehouse.get_total())