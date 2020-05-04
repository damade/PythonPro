import math
from time import time

aList = []


def timePerformance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"it took {t2-t1} ms")
        return result

    return wrapper


# @timePerformance
# @profile()
def checkprime(n):
    j = 2
    while (j <= (n / j)):
        if not (n % j):
            break
        j = j + 1
    if (j > (n / j)):
        print("Prime")
    else:
        print("Not Prime")


def PrimeNumber(n):
    if (n % 2 == 0):
        print("Not Prime")
    else:
        j = math.floor(math.sqrt(n) + 1)
        for i in range(3, j, 2):
            if (n % i == 0):
                print("Not Prime")
                break
        print("Prime")


n = int(input())
for i in range(n):
    item = int(input())
    checkprime(item)
    PrimeNumber(item)
