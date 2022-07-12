employees = int(input('Введите кол-во сотрудников: '))
list_salary = []
for num in range(employees):
    salary = int(input(f'\nЗарплата {num + 1} сотрудника: '))
    list_salary.append(salary)

while 0 in list_salary:
    list_salary.remove(0)
print()
print('\nОсталось сотрудников:', len(list_salary))
print('\nЗарплаты:', list_salary)
print('\nМаксимальная зп:', max(list_salary))
print('Минимальная зп:', min(list_salary))