from datetime import datetime


def logging(func):
    def wrapper(*args, **kwargs):
        print('Запуск функции произошёл в :', datetime.now())
        return func(*args, **kwargs)

    return wrapper


def decorator(cls):
    for i_method in dir(cls):
        if i_method.endswith('__') is False:
            cur_method = getattr(cls, i_method)
            decorated_method = logging(cur_method)
            setattr(cls, i_method, decorated_method)
    return cls


@decorator
class A:
    def test_sum_1(self) -> int:
        print(f'Тут метод test_sim_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


A().test_sum_1()
