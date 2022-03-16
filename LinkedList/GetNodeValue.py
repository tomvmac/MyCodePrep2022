# Problem:
#
# Write a function, get_node_value, that takes in the head of a linked list and an index.
# The function should return the value of the linked list at the specified index.
#
# If there is no node at the given index, then return None.


# Solution:
# 1. Traverse LinkedList
# 2. Keep track of index and when index is == to specified index, return value
# 3. return None otherwise


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_node_value(head, index):
    current = head
    currentIndex = 0
    while current is not None:
        if currentIndex == index:
            return current.val
        current = current.next
        currentIndex += 1

# Driver Code
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 2)) # 'c'