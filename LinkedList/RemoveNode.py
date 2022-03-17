# Problem:
#
# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments.
# The function should delete the node containing the target value from the linked list and return the head of the resulting linked list.
# If the target appears multiple times in the linked list, only remove the first instance of the target in the list.
#
# Do this in-place.
#
# You may assume that the input list is non-empty.
#
# You may assume that the input list contains the target.


# Solution:
# 1. Iterate the list
# 2. Match node val to delete
# 3. Process delete
# 4. return head
#


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


def remove_node_old(head, target):
    index = 0
    current = head
    next = current.next

    while current is not None:
        # edge case for first element
        if current.val == target and index == 0:
            return head.next

        if next is not None:
            if next.val == target:
                # delete node
                current.next = next.next
                return head
        current = current.next
        next = next.next
        index += 1

    return head


def remove_node(head, target):
    current = head
    previous = Node("")

    if current.val == target:
        return head.next

    while current is not None:
        if current.val == target:
            # delete node
            previous.next = current.next
            return head

        previous = current
        current = current.next

    return head


# Driver Code

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

# linked_list_values(remove_node(a, "c"))
# a -> b -> d -> e -> f


q = Node("q")
r = Node("r")
s = Node("s")

q.next = r
r.next = s

# q -> r -> s

linked_list_values(remove_node(q, "q"))
# r -> s

