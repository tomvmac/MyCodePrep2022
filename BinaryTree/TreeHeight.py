# Problem:
#
# Write a function, how_high, that takes in the root of a binary tree.
# The function should return a number representing the height of the tree.
#
# The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.
#
# If the tree is empty, return -1.

# Solution:
# 1. DFS
# 2. Take max of height between two children, and add 1
# 3. Keep bubbling up until root


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def how_high(node):
  if node is None:
    return -1

  left_height = how_high(node.left)
  right_height = how_high(node.right)
  return 1 + max(left_height, right_height)


# Driver Code
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

print(how_high(a)) # -> 2