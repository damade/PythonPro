#!/bin/python3


def checkConseOnes(s):
    k = len(s)
    finalValue = 1
    # form a new string of k 1's
    for i in range(1, k):
        new = "1" * i
        # if there is k 1's at any position
        if new in s:
            finalValue = i
        else:
            continue
    return finalValue


if __name__ == '__main__':
    n = int(input())
    try:
        binaryValue = bin(n)
        print(binaryValue)
        word = str(binaryValue)
        print(word)
        print(f"{checkConseOnes(word)}")
    except (ValueError, TypeError) as e:
        pass
