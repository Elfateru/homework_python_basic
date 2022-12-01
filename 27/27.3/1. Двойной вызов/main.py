from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """
    Декоратор do_twice, которой вызывает декорируемую функцию 2 раза
    """

    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        func(*args, **kwargs)
        return

    return wrapped_func


@do_twice
def func_1(name):
    print(f'Hello {name}')


new_name = input('Введите имя: ')
func_1(new_name)
