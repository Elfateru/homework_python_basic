words = input('Введите строку: ')
new_words = []
count = 0

for i in words:
    if i == ':':
        new_words.append(';')
        count += 1
        continue
    new_words.append(i)

print('Исправленная строка: ', end = '')
for new_sym in new_words:
    print(new_sym, end = '')
print()

print('Кол-во замен: ', count)