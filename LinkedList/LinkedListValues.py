# Problem:
#
# Write a function, linked_list_values, that takes in the head of a linked list as an argument.
# The function should return a list containing all values of the nodes in the linked list.


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




# Driver Code
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

linked_list_values(a)
linked_list_values(None)
