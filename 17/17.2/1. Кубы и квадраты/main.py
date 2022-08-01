num_start = int(input('Левая граница: '))
num_stop = int(input('Правая граница: '))
print()

num_cube = [x ** 3 for x in range(num_start, num_stop + 1)]
num_square = [x ** 2 for x in range(num_start, num_stop + 1)]

print(f'Список кубов чисел в диапазоне от {num_start} до {num_stop}: {num_cube}')
print(f'Список квадратов диапазоне от {num_start} до {num_stop}: {num_square}')