import os
#
# file_name_one = 'group_1.txt'
# file_name_second = 'group_2.txt'
path_1 = os.path.abspath(os.path.join(
    os.path.sep, 'task', 'group_1.txt'))
path_2 = os.path.abspath(os.path.join(
    os.path.sep, 'task', 'Additional_info',
    'group_2.txt'))
print(path_1)
print(path_2)
summ = 0
diff = 0
compose = 1

file_one = open(path_1, 'r', encoding='utf8')
file_second = open(path_2, 'r', encoding='utf8')

for i_elem in file_one:
    temp = i_elem.split()
    summ += int(temp[2])
    diff -= int(temp[2])
file_one.close()

for i_elem in file_second:
    temp = i_elem.split()
    compose *= int(temp[2])
file_second.close()

print(summ)
print(diff)
print(compose)