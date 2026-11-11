# Create a class Player with:
# 	attributes: name, health, attack_power
# 	method: attack(enemy)
# Implement:
# 	__str__()
# 	__add__() → combine attack powers
# 	__sub__() → reduce health after attack
# 	__gt__() → compare health
# 	__eq__() → compare attack power
# 	__getattr__() → return custom message for unavailable player stat
# 	__setattr__() → health cannot go below 0

class Player:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health = enemy.health - self.attack_power
        print(self.name, "attacked", enemy.name)

    def __str__(self):
        return "Name: " + self.name + ", Health: " + str(self.health) + ", Attack Power: " + str(self.attack_power)
    def __add__(self,other):
        return self.attack_power+other.attack_power
    def __sub__(self,other):
        return self.health-other.attack_power
    def __gt__(self,other):
        return self.health>other.health
    def __eq__(self,other):
        return self.attack_power == other.attack_power
    def __getattr__(self,name):
        return "Player stat '" + name + "' is not available"

    def __setattr__(self, name, value):
        if name == "health":
            if value < 0:
                value = 0
        object.__setattr__(self, name, value)


p1 = Player("Arjun", 100, 30)
p2 = Player("Ravi", 80, 20)

print(p1)
print(p2)

p1.attack(p2)
print(p2)

print("Combined attack power:", p1 + p2)

print("Health difference:", p1 - p2)

print("p1 health > p2 health:", p1 > p2)

print("Same attack power:", p1 == p2)

print(p1.mana)

p2.health = -50
print(p2)