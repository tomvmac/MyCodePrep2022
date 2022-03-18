# Problem:
#
# Write a function, depth_first_values, that takes in the root of a binary tree.
# The function should return a list containing all values of the tree in depth-first order.

# Solution:

# 1. Starting with the root, call it current, push on stack
# 2. push right and left children of current or root to stack
# 3. pop stack and process


# Complexity Analysis:

# Time: O(n), n is # of nodes
# Space: O(n)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values_iterative(root):
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values


def depth_first_values_recursive(root):
    if not root:
        return []

    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)
    return [root.val, *left_values, *right_values]


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

print(depth_first_values_iterative(a))
print(depth_first_values_recursive(a))
