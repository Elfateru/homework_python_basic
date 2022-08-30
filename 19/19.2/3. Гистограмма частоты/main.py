# text = input('Введите текст: ')
#
# new_dict = {}
#
# for sym in text:
#     if sym in new_dict:
#         new_dict[sym] += 1
#     else:
#         new_dict[sym] = 1
#
# print(new_dict)
# for letter, freq in new_dict.items():
#     print(letter, ':', freq)
# print('Максимальная частота', max(new_dict.values()))

text = input("Введите текст: ")

frequency = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1

for letter, freq in sorted(frequency.items()):
    print(letter, ':', freq)

print("Максимальная частота: ", max(frequency.values()))