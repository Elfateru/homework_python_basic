from random import randint
nums_list = [randint(1, 10) for _ in range(3)]
iter_num = iter(nums_list)

while True:
    try:
        print(next(iter_num))
    except StopIteration:
        print('Конец')
        break

