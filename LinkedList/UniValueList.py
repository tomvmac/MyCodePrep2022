# Problem:
#
# Write a function, is_univalue_list, that takes in the head of a linked list as an argument.
# The function should return a boolean indicating whether or not the linked list contains exactly one unique value.
#
# You may assume that the input list is non-empty.


# Solution:
#
# 1. Iterate through list
# 2. Store first item value
# 3. if any item value is different from the first item value, then return False

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def is_univalue_list(head):
    current = head
    uniqueVal = current.val
    current = current.next

    while current is not None:
        if current.val != uniqueVal:
            return False
        current = current.next

    return True



# Driver Code

u = Node(2)
v = Node(2)
w = Node(3)
x = Node(3)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

print(is_univalue_list(u))


u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 2 -> 2 -> 2

print(is_univalue_list(u)) # True