# Problem:
#
# Write a function, all_tree_paths, that takes in the root of a binary tree.
# The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.
#
# The order within an individual path must start at the root and end at the leaf,
# but the relative order among paths in the outer list does not matter.
#
# You may assume that the input tree is non-empty.

# Solution:
# 1. DFS
# 2. Find each left node and set 2 dimensional array containgin only leaf [[leaf]]
# 3. Bubble up, combine left and right nodes to parent, concat arrays together
# 4. Null nodes are []

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    paths = []

    left_sub_paths = all_tree_paths(root.left)
    for sub_path in left_sub_paths:
        paths.append([root.val, *sub_path])

    right_sub_paths = all_tree_paths(root.right)
    for sub_path in right_sub_paths:
        paths.append([root.val, *sub_path])

    return paths

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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

print(all_tree_paths(a)) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]