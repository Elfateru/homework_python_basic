class Robot:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.__model)

    def operate(self):
        print('Робот катается по полу как ебанутый')


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun

    def operate(self):
        print('Робот охраняет военный объект при помощи {}'.format(self.__gun))


class VacuumCleaningRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        super().operate()
        print('Робот пылесосит')


class SubmarineRobot(WarRobot):
    def __init__(self, model, gun, depth):
        super().__init__(model, gun)
        self.__depth = depth

    def operate(self):
        super().operate()
        print('Охрана ведётся на глубине {} метров'.format(self.__depth))

sub = SubmarineRobot('U-571', 'Tordedo_001', 250)
print(sub)
sub.operate()
w_robot = WarRobot('MK-1', 'Gun_mk1')
print(w_robot)
w_robot.operate()
cleaner_robo = VacuumCleaningRobot('BObby')
print(cleaner_robo)
cleaner_robo.operate()