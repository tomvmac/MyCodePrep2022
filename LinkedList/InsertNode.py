# Problem:
#
# Write a function, insert_node, that takes in the head of a linked list, a value, and an index.
# The function should insert a new node with the value into the list at the specified index.
# Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.


# Solution:
# 1. Iterate through list and count index position
# 2. When index matches, perform insert

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


def insert_node(head, value, indexPosition):
    current = head
    prev = Node(None)
    prev.next = current
    insertNode = Node(value)
    index = 0

    if head is None:
        return insertNode

    # handle 0 index condition
    if indexPosition == 0:
        insertNode.next = current
        head = insertNode
        return head

    while current is not None:
        if index == indexPosition:
            # perform insert
            prev.next = insertNode
            insertNode.next = current

        prev = prev.next
        current = current.next

        if current is not None:
            index += 1

    if indexPosition > index:
        prev.next = insertNode

    return head



# Driver Code
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
#
# a.next = b
# b.next = c
# c.next = d

# a -> b -> c -> d

# linked_list_values(insert_node(a, 'x', 2))
# a -> b -> x -> c -> d



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(insert_node(a, 'm', 4))
# a -> b -> c -> d -> m