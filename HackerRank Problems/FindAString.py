def count_substring(string, sub_string):
    k = len(string)
    finalValue = 0
    for j in range(k):
        new = sub_string
        # if there is k 1's at any position
        if new in string:
            finalValue += 1
            print(string)
        else:
            continue
    return finalValue


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
