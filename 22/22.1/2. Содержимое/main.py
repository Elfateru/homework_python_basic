import os

abs_path = os.path.abspath(os.path.join('..', '..'))
print('Содержимое каталога', abs_path)
for i_elem in os.listdir(abs_path):
    # print(os.path.abspath(os.path.join('..', '..', i_elem)))
    path = os.path.join(abs_path, i_elem)
    print(path)