from time import sleep

def slow_it_now(_func=None, *, n=1):
    def wrap_func(func):
        def wrapper(*args, **kwargs):
            sleep(n)
            result = func(*args, **kwargs)
            return result
        return wrapper
    if _func is None:
        return wrap_func
    return wrap_func(_func)



@slow_it_now(n=3)
def test() -> None:
    print('Тест')


test()