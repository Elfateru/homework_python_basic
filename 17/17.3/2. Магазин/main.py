count_1 = 0
count_2 = 0

first_word = input('Первое сообщение: ')

count_1 += list(first_word).count('!')
count_1 += list(first_word).count('?')

second_word = input('Второе сообщение: ')

count_2 += list(second_word).count('!')
count_2 += list(second_word).count('?')


if count_1 > count_2:
    print('Третье сообщение:', first_word, second_word)
elif count_1 < count_2:
    print('Третье сообщение:', second_word, first_word)
else:
    print('Ой')
