path = input('Путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
file_extansion = input('Требуемое расширение файла: ')

if path.startswith(disk) and path.endswith(file_extansion):
    print('Путь корректен')
else:
    print('Путь некорректен!')
