def solve(s):
    newString = ""
    splitArray = s.split(' ')
    for item in splitArray:
        if (item.isdigit()):
            newString += (item + " ")
        else:
            newString += (item.capitalize() + " ")
    return newString


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
