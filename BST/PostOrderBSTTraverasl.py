# Problem:
#
# Write a function, post_order, that takes in the root of a binary tree.
# The function should return a list containing the post-ordered values of the tree.
#
# Post-order traversal is when nodes are recursively visited in the order: left child, right child, self.

# Solution:
# 1. Post Order traversal = (left, right, root)

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def post_order(root):
  values = []
  post_order_traversal(root, values)
  return values

def post_order_traversal(root, values):
  if root is None:
    return
  post_order_traversal(root.left, values)
  post_order_traversal(root.right, values)
  values.append(root.val)


x = Node('x')
y = Node('y')
z = Node('z')

x.left = y
x.right = z

#       x
#    /   \
#   y      z

print(post_order(x))
# ['y', 'z', 'x']