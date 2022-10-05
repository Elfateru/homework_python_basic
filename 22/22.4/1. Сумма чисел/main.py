number_sum = 0

file_from = open('new_file.txt', 'r')
print('Содержимое файла new_file.txt:')
for i_line in file_from:
    temp = i_line.rstrip()
    print(temp)
    number_sum += int(temp)
file_from.close()

file_to = open('answer.txt', 'w')
file_to.write(str(number_sum))
file_to = open('answer.txt', 'r')
data = file_to.read()
file_to.close()
print('\nСодержимое файла answer.txt:')
print(data)
