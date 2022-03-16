# Problem:
#
# Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments.
# The function should merge the two lists together into single sorted linked list.
# The function should return the head of the merged linked list.
#
# Do this in-place, by mutating the original Nodes.
#
# You may assume that both input lists are non-empty and contain increasing sorted numbers.

# Solution:
# 1. Loop through both lists l1 and l2 until current1 or current2 is None
# 2. Assign current1, current2, tail
# 2. Compare current1 and current2 vals, for the less one, assign tail to it and tail next to the greater one


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


def merge_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head
    current_1 = head_1
    current_2 = head_2

    while current_1 is not None and current_2 is not None:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next
        tail = tail.next

    if current_1 is not None: tail.next = current_1
    if current_2 is not None: tail.next = current_2

    return dummy_head.next

# Driver Code
a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

mergedHead = merge_lists(a, q)
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28

linked_list_values(mergedHead)
