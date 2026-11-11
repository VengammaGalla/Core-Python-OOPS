class Character:

    def __init__(self, health, max_health):
        self.__health = health
        self.__max_health = max_health

    def damage(self, points):
        self.__health = self.__health - points

        if self.__health < 0:
            self.__health = 0

    def heal(self, points):
        self.__health = self.__health + points

        if self.__health > self.__max_health:
            self.__health = self.__max_health

    @property
    def health(self):
        return self.__health
c = Character(100, 100)
print(c.health)
c.damage(30)
print(c.health)
c.damage(100)
print(c.health)
c.heal(50)
print(c.health)
c.heal(100)
print(c.health)

class Character:
    def __init__(self,health,max_health):
        self.__health=health
        self.__max_health=max_health

    def damage(self,points):
        self.__health=self.__health-points

        if self.__health<0:
            self.__health=0

    def heal(self,points):
        self.__health=self.__health+points

        if self.__health>self.__max_health:
            self.__health=self.__max_health
    @property
    def health(self):
        return self.__health