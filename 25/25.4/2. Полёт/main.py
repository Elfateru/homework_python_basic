class CanFly:
    def __init__(self):
        self.altitude = 0
        self.velocity = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity
        )


class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.5


class Missle(CanFly):

    def take_off(self):
        self.altitude = 500
        self.velocity = 1000

    def land_on(self):
        super().land_on()
        self.explosion()

    def explosion(self):
        print('Ракета показала себя великолепно. Только упала не на ту планету (С) Вернер фон Браун')



m = Missle()
print(m)
m.take_off()
print(m)
m.land_on()
print(m)
# m.explosion()
# print(m)
