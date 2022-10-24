class Toyota:

    def __init__(self, color='red', price=1000000, max_speed=200, cur_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.cur_speed = cur_speed

    def print_info(self):
        print(
            'Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}'.format(
                self.color, self.price, self.max_speed, self.cur_speed
            )
        )


new_car = Toyota()
new_car.print_info()
