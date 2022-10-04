import os
import random


def find_path(cur_path, file_name):
    path_list = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            path_list.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_path(path, file_name)
            if result:
                path_list.extend(result)
    return path_list


def check_file(path):
    file = open(path, 'r', encoding='utf8')
    for line in file:
        print(line, end='')
    file.close()


all_paths = find_path(os.path.abspath(
    os.path.join(os.path.sep,
                 'Users', 'FATE', 'Desktop', 'homework')), 'main.py')
check_file(random.choice(all_paths))
