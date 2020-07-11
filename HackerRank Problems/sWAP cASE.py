def swap_case(s):
    t = s.swapcase()
    return t


def swapCaseAndReverse(s):
    initialWord = s.split(" ")
    theWord = ""
    for i in range(len(initialWord) - 1, -1, -1):
        theWord += (initialWord[i] + " ")
    t = theWord.swapcase()
    return t


if __name__ == '__main__':
    s = input()
    # result = swap_case(s)
    result = swapCaseAndReverse(s)
    print(result)
