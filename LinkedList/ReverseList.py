# Problem:
#
# Write a function, reverse_list, that takes in the head of a linked list as an argument.
# The function should reverse the order of the nodes in the linked list in-place and
# return the new head of the reversed linked list.

# Solution:
# 1. Traverse LinkedList
# 2. Keep track of prev, current and next
# 3. point current.next to prev and move pointers


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

def linked_list_values(head):

    current = head

    while current is not None:
        print(current.val)
        current = current.next

    return


# Driver Code
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(linked_list_values(reverse_list(a)))