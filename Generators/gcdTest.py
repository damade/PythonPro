""""Decorators supercharges our function. It simply a function that accepts a function,
wraps a function into another function and then enhances it or changes it
Performance is used to test the speed of a program"""

# from math import m
# from math import m
from time import time

from memory_profiler import profile


def timePerformance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"it took {t2-t1} ms")
        return result

    return wrapper


@timePerformance
def longTime():
    for i in range(10000000):
        i * 5


# global divisor = 1
@timePerformance
@profile()
def gcdIteration(a, b):
    divisor = 1
    minValue = min(a, b)
    for i in range(1, minValue + 1):
        if ((a % i == 0) and (b % i == 0)):
            divisor = i
        else:
            continue
    print(f"The greatest common divisor is {divisor}\n")
    return


gcdIteration(192, 240)
