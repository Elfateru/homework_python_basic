# def func_1(x):
#     return x + 10
#
#
# def func_2(func, number):
#     return func(number) * func(number)
#
#
# print(func_2(func_1, 9))

def f_1(x):
    return x + 10


def f_2(func, *args, **kwargs):
    return func(*args, **kwargs) * func(*args, **kwargs)


print(f_2(f_1, 9))
