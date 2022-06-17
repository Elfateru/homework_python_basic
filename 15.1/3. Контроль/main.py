def id(id_employee):
    id_search = int(input('Какой ID ищем? '))
    flag = False
    for check in id_employee:
        if check == id_search:
            flag = True
            break

    if flag is True:
        print('Сотрудник на месте')
    else:
        print('Сотрудник не работает!')

id_employee = []

number_employees = int(input('Кол-во сотрудников в офисе: '))

flag = True
for _ in range(number_employees):
    new_id = int(input('ID сотрудника: '))
    if new_id < 1:
        print('ID сотрудника может быть только положительным')
        flag = False
        break
    else:
        id_employee.append(new_id)
        print()

if flag is True:
    id(id_employee)