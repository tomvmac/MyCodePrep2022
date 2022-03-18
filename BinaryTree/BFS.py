# Problem:
#
# Write a function, breadth_first_values, that takes in the root of a binary tree.
# The function should return a list containing all values of the tree in breadth-first order.

# Solution:
# 1. Use a queue
# 2. Start with the root
# 3. Add root to queue
# 4. Pop queue
# 5. Add current node children to queue
# 6. Do this until queue is empty

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def breadth_first_values(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()

        values.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return values



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


print(breadth_first_values(a))