import random

n = int(input('Длина списка: '))
num_list = [random.randint(1, 100) for _ in range(n)]
a, b = random.randint(1, 5), random.randint(6, 10)
num_list = num_list[:a] + num_list[b + 1:]

print(num_list)
