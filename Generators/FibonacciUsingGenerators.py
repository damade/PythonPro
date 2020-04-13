""""Using Generator to solve Fibonacci sequence
give better and time and space complexity or performance
compared to using loop or recursion process"""


def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


fib = fibo(21)

for item in fib:
    print(item)
