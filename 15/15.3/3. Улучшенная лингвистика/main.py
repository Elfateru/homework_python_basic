words_list = []
words_count = [0, 0, 0]

for word in range(1, 4):
    new_word = input(f'Введите {word} слово: ')
    words_list.append(new_word)

text = input('Слово из текста: ')

while text != 'end':
    for index in range(3):
        if words_list[index] == text:
            words_count[index] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')
for i in range(3):
    print(words_list[i], ':', words_count[i])
