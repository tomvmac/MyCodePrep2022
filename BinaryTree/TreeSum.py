# Problem:
#
# Write a function, tree_sum, that takes in the root of a binary tree that contains number values.
# The function should return the total sum of all values in the tree.


# Solution:
# 1. DFS traversal
# 2. Sum up all values


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    stack = []
    sum = 0

    if root == None:
        return sum

    stack.append(root)

    while stack:
        current = stack.pop()
        sum += current.val

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)


    return sum



# Driver code

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a)) # -> 21