import time


def timer(func):
    count = 0
    start_at = time.time()
    a = func()
    for i in a:
        count += 1
        print(count)
        print(i)
    end_at = time.time()
    return end_at - start_at


def func_1():
    return (x ** 2 ** x for x in range(21))


print(timer(func_1))
