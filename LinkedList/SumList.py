# Problem:
#
# Write a function, sum_list, that takes in the head of a linked list
# containing numbers as an argument. The function should return the total sum
# of all values in the linked list.
#
#
# Solution:
#
# 1. Traverse LinkedList and maintaine a count


# Problem:
#
# Write a function, linked_list_values, that takes in the head of a linked list as an argument.
# The function should return a list containing all values of the nodes in the linked list.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_list(head):
    current = head
    sum = 0

    while current is not None:
        sum += current.val
        current = current.next


    return sum




# Driver Code
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

print(sum_list(a))
