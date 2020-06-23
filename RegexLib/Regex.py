import re


class RegexChecker():
    def __init__(self, strings):
        self.strings = strings

    def isAlnum(self):
        theStrings = self.strings
        regexAlnum = True if re.search(r"^[a-zA-Z0-9_]*$", theStrings) else False
        return regexAlnum

    def isAlpha(self):
        theStrings = self.strings
        regexAlpha = True if re.search(r'[a-z][A-Z]', theStrings) else False
        return regexAlpha

    def isDigit(self):
        theStrings = self.strings
        regexDigit = True if re.search(r'\d', theStrings) else False
        return regexDigit

    def isLower(self):
        theStrings = self.strings
        regexLower = True if re.search(r'[a-z]', theStrings) else False
        return regexLower

    def isUpper(self):
        theStrings = self.strings
        regexUpper = True if re.search(r'[A-Z]', theStrings) else False
        return regexUpper
