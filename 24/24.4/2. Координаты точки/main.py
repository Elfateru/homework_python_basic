class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def print_info(self):
        print('x = {}\ny = {}'.format(self.x, self.y))


new_dot = Point(1, 2)
new_dot_1 = Point(2, 3)
new_dot.print_info()
new_dot_1.print_info()
