text = input("Введите строку: ")
text_unique = set(text)
print(text_unique)
nums = ''
for sym in text_unique:
    if '0' <= sym <= '9':
        nums += sym

print('Различные цифры строки:', nums)