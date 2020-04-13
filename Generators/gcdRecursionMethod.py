""""Decorators supercharges our function. It simply a function that accepts a function,
wraps a function into another function and then enhances it or changes it
Performance is used to test the speed of a program"""

# from math import m
# from math import m
from time import time

from memory_profiler import profile

global divisorR


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
def gcdRecursion(a, b):
    divisorR = 1
    if ((a > 1) and (b > 1)):
        minValue = min(a, b)
        for i in range(2, minValue + 1):
            c = a % i
            d = b % i
            e = int(a / i)
            f = int(b / i)
            if ((c == 0) and (d == 0)):
                divisorR *= i
                gcdRecursion(e, f)
            else:
                continue
    else:
        return divisorR
    return divisorR


# longTime()

something = gcdRecursion(4, 16)

print(f"The greatest common divisor is {something}\n")
