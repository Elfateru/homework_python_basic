numbers = []

nums = int(input('Кол-во чисел в списке: '))

for i in range(nums):
    print(f'Введите {i+1} число: ', end = ' ')
    number = int(input())
    numbers.append(number)
    print()
divisor = int(input('Введите делитель: '))
print()
i_summ = 0
count = 0

for i_numbers in numbers:
    if i_numbers % divisor == 0:
        print(f'Индекс числа {i_numbers}: {count}')
        print()
        i_summ += count
    count += 1

print('Сумма индексов: ', i_summ)