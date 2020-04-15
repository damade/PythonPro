class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def __init__(self):
        self.head = None

        # insertion method for the linked list

    def insert(self, head, data):
        newNode = Node(data)
        self.head = head
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next
            current.next = newNode
            return self.head
        else:
            self.head = newNode
            return self.head
    # Complete this method


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);
