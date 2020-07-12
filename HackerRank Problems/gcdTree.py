class Solution(object):
    def maxDiffGCD(self, n, tree):
        if n == -1:
            return -1
        # only root node
        if n == 0:
            return 0

        def findGCD(num1, num2):
            if num2 == 0:
                return num1
            else:
                return findGCD(num2, num1 % num2)

        gcds = []
        for i in range(1, n):
            layer = tree[i]
            for j in range(0, i * 2, 2):
                num1 = max(layer[j], layer[j + 1])
                num2 = min(layer[j], layer[j + 1])
                if num1 == -1 or num2 == -1:
                    continue
                else:
                    gcd = findGCD(num1, num2)
                if not gcds:
                    gcds.append(gcd)
                elif gcd < gcds[0]:
                    gcds = [gcd] + gcds
                elif gcd > gcds[-1]:
                    gcds.append(gcd)
                else:
                    gcds = gcds[:-1] + [gcd] + gcds[-1]

        return gcds[-1] - gcds[0]


s = Solution();
s.maxDiffGCD(2, [1, 2, 3, 4, 6])
