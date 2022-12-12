def repeat(n):
    def wrap_func(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return

        return wrapper

    return wrap_func


@repeat(5)
def greeting(name: str) -> None:
    print(f'Привет {name}!')

greeting('Vasya')