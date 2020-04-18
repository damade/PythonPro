class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution(object):
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def maxDiffGCD(self, n, tree):
        if n == -1:
            return -1
        # only root node
        if n == 0:
            return 0

        def makeList(self, aNode):
            if aNode is None:
                # Stop recursing here
                return []
            return self.makeList(aNode.lChild) + [aNode.data] + self.makeList(aNode.rChild)

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


T = int(input())
myTree = Solution()
root = None
for i in range(1, T + 2):
    if i == 1:
        first = int(input().strip())
        root = myTree.insert(root, first)
    else:
        first = input().strip()
        for j in range(0, i):
            data = int(first.split(" ")[j])
            root = myTree.insert(root, data)
maxDiff = myTree.maxDiffGCD(T, root)
