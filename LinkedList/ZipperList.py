# Problem:
#
# Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
# The function should zipper the two lists together into single linked list by alternating nodes.
# If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
# The function should return the head of the zippered linked list.
#
# Do this in-place, by mutating the original Nodes.
#
# You may assume that both input lists are non-empty.


# Solution:
# 1. Iterate through both lists with a head pointer head1/current1 and head2/current2.
# 2. Store a tail pointer on the iterating list
# 3. Maintain a count, so that we can alternate insertions
# 4. When one of the current pointers hit None, then terminate by pointing the tail to the current1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_lists(head1, head2):

    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    # loop through both lists together
    while current1 is not None or current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        # move pointers
        tail = tail.next
        count += 1

        # terminating case
        if current1 is None:
            tail.next = current2

        if current2 is None:
            tail.next = current1

    return head1

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
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

linked_list_values(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z