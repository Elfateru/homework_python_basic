from abc import ABC

class Figure(ABC):
    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width


    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return f'x: {self.pos_x} y: {self.pos_y} len: {self.length} width: {self.width}'


class ResizeAbleMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Figure, ResizeAbleMixin):
    pass


class Square(Figure, ResizeAbleMixin):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)


s = Rectangle(1, 2, 3, 4)
print(s)