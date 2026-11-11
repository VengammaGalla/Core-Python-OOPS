from abc import ABC, abstractmethod
from copy import deepcopy
class Character(ABC):
    def __init__(self,name,hp,dmg):
        self.name = name
        self._hp = hp
        self.dmg = dmg
        self.__inventory = []

    @property
    def health(self):
        return self._hp

    @property
    def storage(self):
        return deepcopy(self.__inventory)

    @health.setter
    def health(self,n):
        if n >=0 :
            self._hp = n
        elif n < 0:
            self._hp = 0
        else:
            print("Invalid Hp")

    @abstractmethod
    def attack(self,target,reason='combat'):
        pass

    def __add__(self, other):
        if self.item_validator(other):
            self.__inventory.append(other)
        return self

    def __sub__(self, other):
        if other in self.__inventory:
            self.__inventory.remove(other)
        return self

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.health}"

    def __repr__(self):
        return f"Invertory: {self.__inventory}"

    @staticmethod
    def item_validator(item):
        l = ['sword','wand','axe','bow','spear','shield','ropes','grimores']
        return item in l


class Warrior(Character):
    buff = 0.3
    def attack(self,target,reason='combat'):
        atk = self.dmg * (1+self.buff)
        if reason == 'combat':
            target.health -= atk
        print(f"{atk} damage delt by {self.name}")
        print(target)

class Mage(Character):
    buff = 0.2
    def attack(self,target,reason='combat'):
        atk = self.dmg * (1 + self.buff)
        if reason == 'combat':
            target.health -= atk
            print(f"{atk} damage delt by {self.name}")
        print(target)

class Party:
    def __init__(self):
        self.__characters = []

    @property
    def members(self):
        return self.__characters

    def attack(self,target):
        for i in self.__characters:
            i.attack(target)

    def __add__(self, other):
        self.__characters.append(other)
        return self

    def __sub__(self, other):
        if other in self.__characters:
            self.__characters.remove(other)
        return self

    def __len__(self):
        return len(self.__characters)



# w1 = Warrior("Santosh",1000,50)
# w2 = Warrior('Pravallika',1500, 150)
# M1 = Mage('Rajesh', 800, 200)
# m2 = Mage('Keerthi', 800, 180)
#
# mallesh = Party()
# mallesh + w1 + w2 + M1 + m2
#
# print(len(mallesh))
#
# enemy = Warrior('Lokesh', 10000, 300)
# mallesh.attack(enemy)


class Product:
    discount = 0.0
    def __init__(self,id,price):
        self.id = id
        self.__price = price

    def __str__(self):
        return f"id: {self.id} price: {self.__price}"
class Cart:
    def __init__(self):
        self.__items = []

    def add(self,product,qty=1):
        self.__items.append(product)