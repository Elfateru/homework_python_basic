from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """
    Декоратор do_twice, которой вызывает декорируемую функцию 2 раза
    """

    def wrapped_func(*args, **kwargs) -> Any:
        func()
        func()
        return

    return wrapped_func


@do_twice
def func_1():
    print('Hello World')


func_1()
