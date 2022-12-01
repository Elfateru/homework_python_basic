import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        start_at = time.time()
        result = func(*args, **kwargs)
        end_at = time.time()
        run_time = end_at - start_at
        print(f'Функция работала {run_time} секунд')
        return result

    return wrapped_func


@timer
def func_1():
    return (x ** 2 ** x for x in range(20))

