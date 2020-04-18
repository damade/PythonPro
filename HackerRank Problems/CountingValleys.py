#!/bin/python3

# Complete the countingValleys function below.
def countingValleys(n, s):
    k = len(s)
    finalValue = 0
    # form a new string of k 1's
    for j in range(k):
        for i in range(k, 1, -1):
            new = "D" * i
            # if there is k 1's at any position
            if new in s:
                finalValue += 1
                newList = s.partition(new)
                s = newList[0] + newList[2]
                print(s)
            else:
                continue
    return finalValue


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    '''fptr.write(str(result) + '\n')

    fptr.close()'''
    print(result)
