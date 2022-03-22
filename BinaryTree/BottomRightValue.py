# Problem:
#
# Write a function, bottom_right_value, that takes in the root of a binary tree.
# The function should return the right-most value in the bottom-most level of the tree.
#
# You may assume that the input tree is non-empty.


# Solution:
# Look for the right most node of the bottom level

# 1. BFS traverse, going from left to right, last element should right most
# 2. Count levels, until the lowest level
# 3. Right most node

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_right_value(root):
    queue = deque([root])
    current = None

    while queue:
        current = queue.popleft()

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return current.val


a = Node(3)
b = Node(11)
c = Node(10)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

print(bottom_right_value(a)) # -> 1
