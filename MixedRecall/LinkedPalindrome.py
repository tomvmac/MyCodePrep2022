# Problem:
#
# Write a function, linked_palindrome, that takes in the head of a linked list as an argument.
# The function should return a boolean indicating whether or not the linked list is a palindrome.
# A palindrome is a sequence that is the same both forwards and backwards.

# Solution:
# 1. Iterate through LinkedList and add to an array
# 2. Compare the array to the reversed version array, if same, then palindrome

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]

a = Node(3)
b = Node(2)
c = Node(7)
d = Node(7)
e = Node(2)
f = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 2 -> 7 -> 7 -> 2 -> 3
print(linked_palindrome(a)) # True