# Problem:
#
# Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values.
# The function should return the value of the lowest common ancestor of the two values in the tree.
#
# You may assume that the tree values are unique and the tree is non-empty.
#
# Note that a node may be considered an ancestor of itself.

# Solution:
# 1. DFS find path from root to both target, put them into two arrays
# 2. Find 1st common item

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root, val1, val2):
    path1 = get_path(root, val1)
    path2 = get_path(root, val2)
    # convert path2 to set2
    set2 = set(path2)
    for val in path1:
        if val in set2:
            return val

# get_path will produce a list from target to root
def get_path(root, target_val):
    if root is None:
        return None

    if root.val == target_val:
        return [ root.val ]

    left_path = get_path(root.left, target_val)
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    right_path = get_path(root.right, target_val)
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    return None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

print(lowest_common_ancestor(a, 'd', 'h')) # b