first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

even_num = [num for num in range(first_num, second_num + 1) if num % 2 == 0]

print(even_num)
