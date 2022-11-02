class Man:
    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)
        Man.__count += 1

    def __str__(self):
        return f'{self.__name} {self.__age}'
    def set_name(self, value):
        if isinstance(value, str) and value.isalpha():
            self.__name = value
        else:
            raise ValueError('Ошибка имени')

    def set_age(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self.__age = value
        else:
            raise ValueError('Ошибка в возрасте')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age



a = Man('Vaya', 20)
b = Man('regf', 10)
print(a)
print(a._Man__count)