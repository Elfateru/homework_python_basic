class Robot:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        result = super().__str__()
        return result + '{class_name} model {model}'.format(class_name=self.__class__.__name__, model=self.model)

    def operate(self):
        print('Я - Робот')


class CanFly:

    def __init__(self, *args, **kwargs):
        self.altitude = 0
        self.velocity = 0

    def tale_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        result = super().__str__()
        return result + '{class_name} высота {altitude} скорость {velocity}'.format(
            class_name=self.__class__.__name__, altitude=self.altitude, velocity=self.velocity,
        )

class ScoutDrone(CanFly, Robot):

    def __init__(self, model):
        super().__init__(model=model)

    def operate(self):
        super().operate()
        print('Робот ведёт разведку с воздуха')

class WarDrone(CanFly, Robot):
    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print(f'Робот защищает объект при помощи {self.gun}')


ScoutDrone('a1').operate()
WarDrone('Ghost', 'm-264').operate()