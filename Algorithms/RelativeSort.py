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


@timePerformance
@profile()
def RelativeSort(n, arr, listA):
    numberOfSwaps = 0
    # Track number of elements swapped during a single array traversal
    for j in range(0, n - 1):
        # Swap adjacent elements if they are in decreasing order
        if (arr[j] > listA[j]):
            temp = arr[j]
            arr[j] = listA[j]
            listA[j] = temp
            numberOfSwaps += 1;
        else:
            continue
        # If no elements were swapped during a traversal, array is sorted
        if (numberOfSwaps == 0):
            print(f"{numberOfSwaps}")
            break;
    # newArr = arr[:]
    # newListA = listA[:]
    if (arr == sorted(arr) and listA == sorted(listA)):
        print(f"{numberOfSwaps}")
    else:
        print("-1")


if __name__ == '__main__':
    try:
        n = int(input())
        first_list = list(map(int, input().split(",")))
        second_list = list(map(int, input().split(",")))
        RelativeSort(n, first_list, second_list)
    except ValueError:
        print("Input Numbers only")
        pass
