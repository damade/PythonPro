import math
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


# https://leetcode.com/discuss/interview-question/397156/google-oa-summer-intern-2020-relative-sort
@timePerformance
@profile()
def relativeSort(n, A, B):
    # swap, not swap
    dp = [[1, 0]] + [[math.inf, math.inf] for _ in range(n - 1)]
    for i, (a0, a1, b0, b1) in enumerate(zip(A, A[1:], B, B[1:]), 1):
        if a1 > a0 and b1 > b0:
            # last time swapped, this time swap again
            dp[i][0] = min(dp[i][0], 1 + dp[i - 1][0])
            # last time not swapped, this time not swap again
            dp[i][1] = min(dp[i][1], dp[i - 1][1])
        if a1 > b0 and b1 > a0:
            # last time not swapped, this time swap
            dp[i][0] = min(dp[i][0], 1 + dp[i - 1][1])
            # last time swapped, this time not swap
            dp[i][1] = min(dp[i][1], dp[i - 1][0])
        if min(dp[i]) == math.inf: return -1
    return min(dp[-1])


@timePerformance
@profile()
def relativeSort1(n, A, B):
    # swap, not swap
    dp = [1, 0]
    for a0, a1, b0, b1 in zip(A, A[1:], B, B[1:]):
        dp_new = [math.inf, math.inf]
        if a1 > a0 and b1 > b0:
            # last time swapped, this time swap again
            dp_new[0] = min(dp_new[0], 1 + dp[0])
            # last time not swapped, this time not swap again
            dp_new[1] = min(dp_new[1], dp[1])
        if a1 > b0 and b1 > a0:
            # last time not swapped, this time swap
            dp_new[0] = min(dp_new[0], 1 + dp[1])
            # last time swapped, this time not swap
            dp_new[1] = min(dp_new[1], dp[0])
        dp = dp_new
        if min(dp) == math.inf: return -1
    return min(dp)


# n = 4
# A = [1, 4, 4, 9]
# B = [2, 3, 5, 10]
# print(relativeSort(n, A[:], B[:]))
# print(relativeSort1(n, A[:], B[:]))
#
# n = 4
# A = [1, 4, 4, 9]
# B = [2, 3, 1, 10]
# print(relativeSort(n, A[:], B[:]))
# print(relativeSort1(n, A[:], B[:]))
#
# n = 4
# A = [1, 3, 6, 5]
# B = [2, 5, 4, 7]
# print(relativeSort(n, A[:], B[:]))
# print(relativeSort1(n, A[:], B[:]))
#
# n =5
# A = [0,4,4,5,9]
# B = [0,1,6,8,10]
# print(relativeSort(n, A[:], B[:]))
# print(relativeSort1(n, A[:], B[:]))

# n =5
# A = [1,7,6,9,10]
# B = [3,8,5,7,11]
# print(relativeSort(n, A[:], B[:]))
# print(relativeSort1(n, A[:], B[:]))

n = 10
A = [2, 5, 14, 18, 22, 28, 35, 43, 56, 64]
B = [1, 7, 12, 15, 23, 26, 31, 44, 52, 59]
print(relativeSort(n, A[:], B[:]))
print(relativeSort1(n, A[:], B[:]))
