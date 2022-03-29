# Problem:
#
# Pre Order: root, left, right


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def pre_order(root):
  values = []
  pre_order_traversal(root, values)
  return values

def pre_order_traversal(root, values):
  if root is None:
    return
  values.append(root.val)
  pre_order_traversal(root.left, values)
  pre_order_traversal(root.right, values)



x = Node('x')
y = Node('y')
z = Node('z')

x.left = y
x.right = z

#       x
#    /   \
#   y      z

print(pre_order(x))
# ['x', 'y', 'z']