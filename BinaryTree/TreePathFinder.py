# Problem:
#
# Write a function, path_finder, that takes in the root of a binary tree and a target value.
# The function should return an array representing a path to the target value.
# If the target value is not found in the tree, then return None.
#
# You may assume that the tree contains unique values.


# Solution:
# 1. DFS
# 2. Use two base cases
#    a. return when target match is found
#    b. return when null is found
# 3. At each root, if there is a child containing a match, include that and add in the root value

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def path_finder(root, target):
    if root is None:
        return None

    if root.val == target:
        return [root.val]

    left_path = path_finder(root.left, target)
    if left_path is not None:
        return [root.val, *left_path]

    right_path = path_finder(root.right, target)
    if right_path is not None:
        return [root.val, *right_path]


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

print(path_finder(a, 'e'))
# -> [ 'a', 'b', 'e' ]