phone_book = dict()
print('Текущие контакты на телефоне:\n''<Пусто>')
while True:
    name = input('Введите имя: ')
    if name == 'stop':
        break
    elif name in phone_book:
        print('Ошибка такое имя уже существует.')
        continue
    else:
        number = input('Введите номер телефона: ')
        phone_book[name] = number
        print('Текущие контакты на телефоне: ')
        for info in phone_book:
            print(info, phone_book[info])
        print()
