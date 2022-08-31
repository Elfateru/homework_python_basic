import random

nums_1 = [
    29, 17, 10, 15, 13, 22, 12, 22, 7,
    24, 26, 3, 11, 2, 3, 16, 19, 21, 2,
    3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1
]

nums_2 = [
    16, 21, 30, 24, 5, 7, 23, 13, 11, 5,
    21, 5, 19, 9, 12, 9, 15, 16, 29, 8,
    16, 1, 22, 15, 16, 9, 1, 13, 21, 21
]

nums_set_1 = set(nums_1)
nums_set_2 = set(nums_2)
print('Первое множество:', nums_set_1)
print('Второе множество:', nums_set_2)
print()

print('Минимальный элеммент 1-го множества:', min(nums_set_1))
print('Минимальный элеммент 2-го множества:', min(nums_set_2))
print()
nums_set_1.discard(min(nums_set_1))
nums_set_2.discard(min(nums_set_2))

random_num_1 = random.randint(100, 200)
random_num_2 = random.randint(100, 200)
print('Случайное число для 1-го множества:', random_num_1)
print('Случайное число для 2-го множества:', random_num_2)
print()
nums_set_1.add(random_num_1)
nums_set_2.add((random_num_2))
print('Объединение множеств:')
print(nums_set_1.union(nums_set_2))
print(nums_set_1 | nums_set_2)
print()
print('Пересечение множеств: ')
print(nums_set_1.intersection(nums_set_2))
print(nums_set_1 & nums_set_2)
print('Элементы, входящие в nums_2, но не входящие в nums_1:')
print(nums_set_2.difference(nums_set_1))
print(nums_set_2 - nums_set_1)