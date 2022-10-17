BRUCE_WILLIS = 42

input_data = input('Введите строку: ')

try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError as exc:
    print(f'{type(exc)} невозможно преобразовать к числу')
except IndexError as exc:
    print(f'{type(exc)} выход за границы списка')
except Exception as exc:
    print(f'{type(exc)} поймано исключение')

