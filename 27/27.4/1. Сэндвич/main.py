def get_some_salad(func):
    def wrapped_func(*args, **kwargs):
        print('#помидоры#')
        func(*args, **kwargs)
        print('~салат~')

    return wrapped_func


def get_some_buns(func):
    def wrapped_func(*args, **kwargs):
        print('</---------\>')
        func(*args, **kwargs)
        print('<\_____/>')

    return wrapped_func


@get_some_buns
@get_some_salad
def filling_sandwich(filler):
    print('--' + filler + '--')


filling_sandwich('ветчина')
