import textwrap


def wrap(string, max_width):
    theList = textwrap.wrap(string, max_width)
    finalString = ""
    for eachWrap in theList:
        finalString += (eachWrap + "\n")
    return finalString


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
