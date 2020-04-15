# Write your code here
class Calculator:
    def power(self, n, p):
        self.n = n
        self.p = p
        base = self.n
        theExp = self.p
        e = "n and p should be non-negative"
        if ((base >= 0) and (theExp >= 0)):
            return pow(base, theExp)
        else:
            return e


# Exception e = "n and p should be non-negative"
myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
