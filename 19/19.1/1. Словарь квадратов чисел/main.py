num = int(input('Введите число: '))
num_dict = dict()

for n in range(1, num + 1):
    num_dict[n] = n ** 2
print(num_dict)