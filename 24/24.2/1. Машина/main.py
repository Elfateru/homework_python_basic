import random


class Toyota:
    color = 'red'
    price = 1000e3
    max_speed = 200
    cur_speed = 0

first_car = Toyota()
first_car.cur_speed = random.randint(0, 200)

second_car = Toyota()
second_car.cur_speed = random.randint(0, 200)

third_car = Toyota
third_car.cur_speed = random.randint(0, 200)

print(first_car.cur_speed, second_car.cur_speed, third_car.cur_speed)