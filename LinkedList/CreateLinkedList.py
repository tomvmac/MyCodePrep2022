# Problem:
# Write a function, create_linked_list, that takes in a list of values as an argument.
# The function should create a linked list containing each item of the list as the values of the nodes.
# The function should return the head of the linked list.


# Solution:
# 1. Iterate through list
# 2. Add to linkedlist


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):

    current = head

    while current is not None:
        print(current.val)
        current = current.next

    return

def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head
  for val in values:
    tail.next = Node(val)
    tail = tail.next
  return dummy_head.next


# Driver code
linked_list_values(create_linked_list(["h", "e", "y"]))
# h -> e -> y