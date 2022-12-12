from datetime import datetime

def decorator(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)

        print('Время создания -', datetime.now())
        print('Методы:', end='')
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                print(i_method, end=' ')
        print()
        return instance
    return wrapper

@decorator
class Example:

    def hello(self):
        print('hello')

    def bye(self):
        print('bye')


Example()
Example()