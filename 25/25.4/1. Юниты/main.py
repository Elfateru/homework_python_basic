class Unit:
    def __init__(self, hp):
        self.__hp = hp

    def set_hp(self, amount):
        self.__hp = amount

    def get_hp(self):
        return self.__hp

class Soldier(Unit):

    def get_dmg(self, amount):
        self.set_hp(self.get_hp() - amount)

class Citizen(Unit):

    def get_dmg(self, amount):
        self.set_hp(self.get_hp() - amount * 2)

c_1 = Citizen(100)
print(c_1.get_hp())
c_1.get_dmg(20)
print(c_1.get_hp())