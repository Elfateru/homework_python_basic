


class Toyota:
    color = 'red'
    price = 1000e3
    max_speed = 200
    cur_speed = 0

    def print_info(self):
        print('Color: {}\nPrice: {}\n Max speed: {}\n Current speed: {}'.format(
            self.color, self.price, self.max_speed, self.cur_speed)
        )

    def speed_change(self, speed):
        self.cur_speed = speed


new_car = Toyota()
new_car.print_info()
print()
new_car.speed_change(200)
new_car.print_info()
print()
new_car.speed_change(10)
new_car.print_info()