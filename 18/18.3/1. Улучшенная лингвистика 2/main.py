words_list = [input('Введите слово: ') for _ in range(3)]
text = input('Введите текст: ')
words_count = [text.count(word) for word in words_list]

print(words_count)