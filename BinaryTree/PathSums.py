# Problem:
#
# Calculate sums for all paths of the tree.

# Solution:
# 1. Iterate through left and right children recursively
# 2. sum left put into array
# 3. sum right put into array


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_sums(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    paths = []
    sums = []
    sum = 0

    left_sub_paths = path_sums(root.left)
    path_item = []
    for sub_path in left_sub_paths:
        sub_path.append(root.val)
        paths.append(sub_path)

    right_sub_paths = path_sums(root.right)
    for sub_path in right_sub_paths:
        sub_path.append(root.val)
        paths.append(sub_path)

    for path in paths:
        sum = 0
        for item in path:
            # print(item)
            sum += item
        sums.append(sum)

    # print(sums)
    return sums

#           1
#        /    \
#       3      2
#      /  \
#     7    4
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

print(path_sums(a)) #