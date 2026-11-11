class Character:
    stamina_cost = 10

    def __init__(self, name, health):
        self.name = name
        self.__health = health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health cannot be negative")
        self.__health = value

    def attack(self):
        print(self.name, "attacks")


class Warrior(Character):
    stamina_cost = 20

    def attack(self):
        print(self.name, "uses sword attack")


class Archer(Character):
    stamina_cost = 15

    def attack(self):
        print(self.name, "shoots an arrow")


class Mage(Character):
    stamina_cost = 25

    def attack(self):
        print(self.name, "casts a magic spell")


team = [
    Warrior("Thor", 100),
    Archer("Robin", 80),
    Mage("Merlin", 70)
]

for character in team:
    character.attack()
    print("Health:", character.health)
    print("Stamina cost:", character.stamina_cost)