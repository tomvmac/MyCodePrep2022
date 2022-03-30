# Problem:
#
# Write a function, tree_includes, that takes in the root of a binary tree and a target value.
# The function should return a boolean indicating whether or not the value is contained in the tree.


# Solution:
# 1. Traverse tree DFS or BFS
# 2. Check val of current node and return True if target found, otherwise return False


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, target):
    stack = []

    if root is None:
        return False

    stack.append(root)

    while stack:
        current = stack.pop()
        if current.val == target:
            return True

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)


    return False


def tree_include_recur(root, target):
    if root is None:
        return

    if root.val == target:
        return True

    if tree_include_recur(root.left, target) or tree_include_recur(root.right, target):
        return True

    return False

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

print(tree_includes(a, "e")) # -> True
print(tree_include_recur(a, "e"))