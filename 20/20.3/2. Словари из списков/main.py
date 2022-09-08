import random


def get_random_letter():
    return random.choices([chr(i) for i in range(ord('а'), ord('я'))], k=10)

f_list = get_random_letter()
s_list = get_random_letter()
print(f_list)
print(s_list)
print()
f_dict = dict(enumerate(f_list))
s_dict = dict(enumerate(s_list))
print('Первый словарь:', f_dict)
print('Второй словарь:', s_dict)
