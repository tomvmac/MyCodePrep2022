# Problem:
#
# Write a function, linked_list_find, that takes in the head of a linked list and a target value.
# The function should return a boolean indicating whether or not the linked list contains the target.
#
# Solution:
# 1. Traverse list
# 2. return True if match

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_find(head, target):
    current = head

    while current is not None:
        if current.val == target:
            return True
        current = current.next


    return False


# Driver Code
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(linked_list_find(a, "c")) # True
print(linked_list_find(a, "x")) # True
