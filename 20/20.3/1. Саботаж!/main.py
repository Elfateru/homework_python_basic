string = input('Введите строку: ')
print('Ответ: ', end=' ')
for num, sym in enumerate(string):
    if sym == '~':
        print(num, end=' ')
