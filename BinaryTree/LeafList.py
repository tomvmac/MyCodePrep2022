# Problem:
#
# Write a function, leaf_list, that takes in the root of a binary tree and returns
# a list containing the values of all leaf nodes in left-to-right order.

# Solution:
# 1. DFS
# 2. If a node is a leaf then add to leafList


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leaf_list(root):
    if root is None:
        return []

    leaves = []

    stack = [root]
    while stack:
        current = stack.pop()

        if current.left is None and current.right is None:
            leaves.append(current.val)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return leaves

def leaf_list_recur(root, leaves):
    if root is None:
        return []

    current = root
    if current.left is None and current.right is None:
        leaves.append(current.val)

    if current.left is not None:
        leaf_list_recur(current.left, leaves)

    if current.right is not None:
        leaf_list_recur(current.right, leaves)

    return leaves


# Driver Code
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(leaf_list(a)) # -> [ 'd', 'e', 'f' ]
print(leaf_list_recur(a, []))