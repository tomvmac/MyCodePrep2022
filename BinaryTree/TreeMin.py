# Problem:
#
# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values.
# The function should return the minimum value within the tree.
#
# You may assume that the input tree is non-empty.

# Solution:
# 1. Traverse tree DFS or BFS
# 2. Check val of against min and take the smaller of the two


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value(root):
    stack = []
    minValue = None

    if root is None:
        return None

    stack.append(root)

    while stack:
        current = stack.pop()
        if minValue is None:
            minValue = current.val
        else:
            minValue = min(current.val, minValue)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)


    return minValue


# Driver Code
a = Node(3)
b = Node(11)
c = Node(4)
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
#   11     4
#  / \      \
# 4   -2     1
print(tree_min_value(a)) # -> -2