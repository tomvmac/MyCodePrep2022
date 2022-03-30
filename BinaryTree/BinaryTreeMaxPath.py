class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_path(root):
  if root is None:
    return 0

  if root.left is None and root.right is None:
    return 2

  return 1 + max(max_path(root.left), max_path(root.right))

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

a = Node(5)
b = Node(10)
c = Node(20)
d = Node(8)
e = Node(10)
f = Node(3)
g = Node(7)

print(max_path(a)) # -> 3


a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

a = Node(1)
b = Node(3)
c = Node(2)
d = Node(7)
e = Node(8)
f = Node(9)
g = Node(4)
h = Node(5)
i = Node(6)

a.left = b
a.right = c
b.left = d
d.left = e
e.left = f
b.right = g
g.right = h
h.right = i

print(max_path(a)) # -> 6