# Problem:
#
# Write a function, lefty_nodes, that takes in the root of a binary tree.
# The function should return a list containing the left-most value on every level of the tree.
# The list must be ordered in a top-down fashion where the root is the first item.



# Solution:
# - Left most node doens't have to be on the left child
# - Must track level, usually by incrementing as you recurse

# 1. DFS
# 2. Track level as we traverse
# 3. The first node accessed on any level should be the left most node.  If the node whose index on the array is already there for that level, do NOT add it
# 4. Only add if the node for level is not in the array.


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def lefty_nodes(root):
  values = []
  traverse(root, 0, values)
  return values


def traverse(root, level, values):
  if root is None:
    return

  if len(values) == level:
    values.append(root.val)

  traverse(root.left, level + 1, values)
  traverse(root.right, level + 1, values)

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

print(lefty_nodes(a)) # [ 'a', 'b', 'd', 'g' ]
