import random

def create_random_tuple(a, b):
    return tuple([random.randint(a, b) for _ in range(10)])

first_tuple = create_random_tuple(0, 5)
second_tuple = create_random_tuple(-5, 0)
third_tuple = first_tuple + second_tuple
nulls_count = third_tuple.count(0)

print(third_tuple, nulls_count)
