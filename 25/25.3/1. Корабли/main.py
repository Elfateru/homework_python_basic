class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\nмодель корабля: {}'.format(self.__model)

    def sail(self):
        print('\nКорабль {} куда-то уплыл'.format(self.__model))

class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('Корабль атакует с помощью оружия', self.gun)

class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('\nЗагружаем корабль!')
        self.tonnage_load += 1
        print('\nТекущая загруженность {}'.format(self.tonnage_load))

    def unload(self):
        if self.tonnage_load > 0:
            print('\nРазгрудаем корабль')
            self.tonnage_load -= 1
        else:
            print('Корабль уже разгружен!')
        print('Текущая загруженность {}'.format(self.tonnage_load))


warship = WarShip('MetallGear', 'm254')
print(warship)
warship.attack()
warship.sail()
cargoship = CargoShip('Deer')
print(cargoship)
cargoship.unload()
cargoship.load()
cargoship.unload()