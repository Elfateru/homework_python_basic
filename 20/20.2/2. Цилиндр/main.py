import math

radius_input = int(input('Введите радиус: '))
height_input = int(input('Введите высоту: '))

def cylinder(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * math.pi * r ** 2
    return side, full

side_area, full_area = cylinder(radius_input, height_input)
print(round(side_area, 2), round(full_area, 2))
