class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, word):
        self._name = word

    @age.setter
    def age(self, value):
        self._age = value

    def __repr__(self):
        return f'{self._name}, {self._age}'


man_1 = Person('Max', 21)
man_2 = Person('Alex', 20)
man_3 = Person('Anton', 22)
mans_list = [man_1, man_2, man_3]
print(mans_list)
mans_list.sort(key=lambda x: -x.age)
print(mans_list)
mans_list.sort(key=lambda x: x.age)
print(mans_list)
