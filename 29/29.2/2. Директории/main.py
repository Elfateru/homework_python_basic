from contextlib import contextmanager
import os

@contextmanager
def in_dir(path):
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cur_path)


with in_dir('d:\\'):
    print(os.listdir())