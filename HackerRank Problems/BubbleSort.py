#!/bin/python3

def BubbleSort(a, n):
    numberOfSwaps = 0;
    for i in range(0, n):
        # Track number of elements swapped during a single array traversal
        for j in range(0, n - 1):
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                numberOfSwaps += 1;
        # If no elements were swapped during a traversal, array is sorted
        if (numberOfSwaps == 0):
            break;
    print(f"Array is sorted {numberOfSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")
    return


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
BubbleSort(a, n)
# Write Your Code Here
