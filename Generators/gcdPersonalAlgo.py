""""Decorators supercharges our function. It simply a function that accepts a function,
wraps a function into another function and then enhances it or changes it
Performance is used to test the speed of a program"""

# from math import m
# from math import m
from time import time

from memory_profiler import profile


# global divisorR
# global divisor
#
# divisorR = 1
# divisor = 1

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
def gcdMyAlgo(a, b, divisorR, divisor):
    minValue = min(a, b)
    if ((a % 2 == 0) and (b % 2 == 0)):
        divisorR *= 2
        c = int(a / 2)
        d = int(b / 2)
        gcdMyAlgo(c, d, divisorR, divisor)
    else:
        minValue = min(a, b)
        for i in range(1, minValue + 1):
            if ((a % i == 0) and (b % i == 0)):
                divisor = i
            else:
                continue
    return divisorR, divisor


# longTime()

something = gcdMyAlgo(192, 240, 1, 1)

print(f"The greatest common divisor is {something}\n")
