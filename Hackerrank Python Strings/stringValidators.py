import RegexLib.Regex as reg

if __name__ == '__main__':
    s = input()
    regChecker = reg.RegexChecker(s)  # instantiating the RegexLibClass

    # Using more like a ternary operator(there is no ternary operator in Python)
    print(True if any(x.isalnum() for x in s) else False)
    print(True if any(x.isalpha() for x in s) else False)
    print(True if any(x.isdigit() for x in s) else False)
    print(True if any(x.islower() for x in s) else False)
    print(True if any(x.isupper() for x in s) else False)

    # Using Regex Libraries i created.
    print(regChecker.isAlnum())
    print(regChecker.isAlpha())
    print(regChecker.isDigit())
    print(regChecker.isLower())
    print(regChecker.isUpper())
