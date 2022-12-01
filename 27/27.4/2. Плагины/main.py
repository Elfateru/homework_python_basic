from typing import Dict, Callable

PLUGINS: Dict[str, Callable] = dict()


def go_to_plugins(func: Callable) -> Callable:
    """ Декоратор. Регистрирует функцию как плагин"""
    PLUGINS[func.__name__] = func
    return func


@go_to_plugins
def hello(name: str) -> str:
    return f'Hello {name}'


@go_to_plugins
def goodbye(name: str) -> str:
    return f'Goodbye {name}'


print(PLUGINS)
print(hello('Tom'))
print(goodbye('Tom'))
