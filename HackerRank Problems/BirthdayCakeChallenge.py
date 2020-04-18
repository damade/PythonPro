#!/bin/python3

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count = {}
    for i in ar:
        count.setdefault(i, 0)
        count[i] = count[i] + 1
    sorted(count.values())
    newArr = []
    for v in sorted(count.values()):
        newArr += [v]
    return newArr[len(newArr) - 1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(f"{result}")

    '''fptr.write(str(result) + '\n')

    fptr.close()'''
