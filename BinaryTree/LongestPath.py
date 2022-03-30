# Problem:
# Find the longest path within the tree.  It doesn't need to be from the root

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def longest_path(root):
  if root is None:
    return 0

  if root.left is None and root.right is None:
    return 0

  return 1 + longest_path(root.left) + longest_path(root.right)

def longest_path_from_root(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 0

    return 1 + max(longest_path_from_root(root.left),longest_path_from_root(root.right))


#           1
#        /    \
#       3      2
#      /  \      \
#     7    4     15
#    /      \
#   8        5
#  /          \
# 9            6


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

print(longest_path(a)) # -> 6
print(longest_path_from_root(a)) # -> 4