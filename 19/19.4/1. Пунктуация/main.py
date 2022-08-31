text = input('Введите строку: ')

symbols = set(".,;:!?")

count = 0
for sym in text:
    if sym in symbols:
        count += 1
print(f'Количество знаков пунктуации: {count}')
