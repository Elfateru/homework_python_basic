import os


path_to = input('Введите путь: ')

if os.path.isdir(path_to):
    print('Это директория')
elif os.path.isfile(path_to):
    print('Это файл')
    print('Размер файла:', os.path.getsize(path_to), 'байт')
else:
    print('Указанного файла не существует')
