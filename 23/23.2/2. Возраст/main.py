file_age = None
file_result = None

try:
    file_age = open('ages.txt', 'r')
    file_result = open('result.txt', 'x', encoding='utf8')
except (PermissionError, FileExistsError) as exc:
    print('Исключение: ', exc, type(exc))
except IsADirectoryError:
    print('На чтение ожидался файл, но это оказалась директория.')

if file_age and file_result:
    names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    count = 0
    for i_line in file_age:
        try:
            int(i_line)
            file_result.write(names[count] + '-' + i_line)
            count += 1
        except (ValueError, TypeError, AttributeError) as exc:
            print('Исключение: ', exc, type(exc))
    file_result.close()
file_age.close()
