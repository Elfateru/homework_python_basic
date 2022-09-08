phone_dict = dict()
while True:
    name = input('Введите имя: ')
    if name == 'стоп':
        break
    last_name = input('Введите фамилию: ')

    last_name_name = last_name, name
    if last_name_name not in phone_dict:
        phone_dict[last_name_name] = int(input('Введите номер: '))
    else:
        print('Такой человек уже есть!')
    print('Текущий словарь контактов:', phone_dict)