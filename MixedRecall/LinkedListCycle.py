# Problem:
#
# Write a function, linked_list_cycle, that takes in the head of a linked list as an argument.
# The function should return a boolean indicating whether or not the linked list contains a cycle.

# Solution:
# 1. Use two pointers, slow and fast
# 2. slow moves 1 step, fast moves 2
# 3. if fast == slow then we have a cycle
# 4. if fast hits null then no cycle

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_cycle(head):
    first_iteration = True

    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        if slow is fast and not first_iteration:
            return True
        first_iteration = False
        slow = slow.next
        fast = fast.next.next

    return False


q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')

q.next = r
r.next = s
s.next = t
t.next = u
u.next = t # cycle

#                   __
#                 /   \
# q -> r -> s -> t -> u

# print(linked_list_cycle(q))  # True


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_cycle(a))  # False


# p = Node('p')

# p

# print(linked_list_cycle(p)) # False