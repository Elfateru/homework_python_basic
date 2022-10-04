import os.path

def find_file(cur_path, file):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem == file:
            print(path, i_elem)
        if os.path.isdir(path):
            result = find_file(path, file)
            if result:
                break
    else:
        result = None

    return result

file_path = os.path.abspath(os.path.join('..', '..'))
print('Ищем в', file_path)
file_name = 'main.py'
print('\nИмя файла:', file_name)
print('\nНайдены следующие пути:\n')
find_file(file_path, file_name)
