class Point:

    def __init__(self, x, y):
        self.__x = 0
        self.__y = 0
        self.set_x(x)
        self.set_y(y)

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__x = float(checker_value)

    def set_y(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__y = float(checker_value)

    def check_value(self, value):
        if isinstance(value, str) and value.isdigit():
            return value
        if isinstance(value, (int, float)):
            if value == 0:
                value = str(value)
            return value
        return None


a = Point('2', '1')
print(a)
print(a.get_y())
