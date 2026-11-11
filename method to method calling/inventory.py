class Inventory:
    total=0
    threshold=20
    def __init__(self):
        self.stock={}
    def add(self,item,qty):
       if self.valid(qty):
           self.stock[item]=qty
           Inventory.total += 1
           self.display()
       else:
           print("qty is more")
    def remove(self,item):
        if item in self.stock:
            self.stock.pop(item)
            Inventory.total -= 1
            self.display()
        else:
            print(f"{item} not found")
    @classmethod
    def update(cls,nt):
        cls.threshold=nt
    @staticmethod
    def valid(qty):
        return qty>=Inventory.threshold
    def display(self):
        print("Item:qty")
        for i,j in self.stock.items():
            print(f"{i} : {j}")
        print(f"minimum_threshold:{Inventory.threshold}")
        print("Total Items:", Inventory.total)
s1 = Inventory()

# Adding items
s1.add("Beans", 100)
s1.add("Rice", 50)

# Removing item
s1.remove("Beans")

# Updating threshold
Inventory.update(30)

# Display inventory
s1.display()





