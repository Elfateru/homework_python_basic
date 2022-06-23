word = input('Введите строку: ')
num_sym = int(input('Номер символа: '))

word_list = list(word)
count = 0
if 0 < num_sym <= len(word):
    if num_sym == 1:
        print('Символа слева нет')
    else:
        print('Символ слева: ', word_list[num_sym-2])
        if word_list[num_sym - 2] == word_list[num_sym - 1]:
            count += 1
    if num_sym == len(word):
        print('Символа справа нет')
    else:
        print('Символ справа: ', word_list[num_sym])
        if word_list[num_sym - 1] == word_list[num_sym]:
            count += 1

    if count == 1:
        print('Есть ровно один такой же символ.')
    elif count == 2:
        print('есть два таких же символа')
    else:
        print('Таких же символов нет.')
