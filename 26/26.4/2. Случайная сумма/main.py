from random import random


class SumsOfLastTwo:
    def __init__(self, count):
        self.last = 0
        self.end = count
        self.start = 0

    def __iter__(self):
        self.last = 0
        self.start = 0
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        self.last += random()
        return self.last


counter = SumsOfLastTwo(5)
for j, i in enumerate(counter):
    print(j, round(i, 2))
for j, i in enumerate(counter):
    print(j, round(i, 2))
