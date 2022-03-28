# Problem:
#
# Write a function, middle_value, that takes in the head of a linked list as an argument.
# The function should return the value of the middle node in the linked list.
# If the linked list has an even number of nodes, then return the value of the second middle node.
#
# You may assume that the input list is non-empty.

# Solution:
# 1. Use two pointers, slow and fast
# 2. slow moves one step, fast pointer moves two steps
# 3. when fast pointer hits null and fast next  is null, slow pointer is exactly at mid point
#
# Time:
# O(n)
#
# Space:
# O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def middle_value(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next


    return slow.val



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.next = b
b.next = c
c.next = d
d.next = e

# a -> b -> c -> d -> e
print(middle_value(a)) # c

x = Node('x')
y = Node('y')

x.next = y

# x -> y
print(middle_value(x)) # y