def Solution():
    n = int(input())

    maxGCD = float('-inf')
    minGCD = float('inf')

    for i in range(0, n + 1):
        if i == 0:
            input()
        else:
            for j in range(0, 2 ** i, 2):
                a = input()
                b = input()
                if (a == -1 or b == -1):
                    continue

                newGCD = gcd(a, b)
                if newGCD < minGCD:
                    minGCD = newGCD
                if newGCD > maxGCD:
                    maxGCD = newGCD

    if (minGCD == float('inf') and maxGCD == float('-inf')):
        print(0)
        return

    print(maxGCD - minGCD)


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


Solution()
