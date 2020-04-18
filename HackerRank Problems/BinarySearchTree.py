class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
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

    def getLongestNodePath(self, root):
        count = 1
        if root == None:
            return 0
        else:
            treeHeight = 1 + max(self.getLongestNodePath(root.left), self.getLongestNodePath(root.right))
            return treeHeight

    def getHeight(self, root):
        lnp = self.getLongestNodePath(root)
        return lnp - 1
        # Write your code here


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
