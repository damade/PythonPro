""""Decorators supercharges our function. It simply a function that accepts a function,
wraps a function into another function and then enhances it or changes it
Performance is used to test the speed of a program"""

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"it took {t2-t1} ms")
        return result

    return wrapper


@performance
def longTime():
    for i in range(100000000000000000):
        i * 5


longTime()
