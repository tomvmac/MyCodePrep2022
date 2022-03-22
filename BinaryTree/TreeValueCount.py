# Problem:
#
# Write a function, tree_value_count, that takes in the root of a binary tree and a target value.
# The function should return the number of times that the target occurs in the tree.
#
#
# Solution:
#
# 1. DFS Traverse binary tree
# 2. Keep an targetCount and increment for each value that matches the target


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def tree_value_count(root, target):
    targetCount = 0

    if root is None:
        return targetCount

    stack = [root]

    while stack:
        current = stack.pop()
        if current.val == target:
            targetCount += 1

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return targetCount


def tree_value_count_recur(root, target, targetCount):

    if root is None:
        return targetCount

    current = root

    if current.val == target:
        targetCount += 1

    if current.right is not None:
        targetCount = tree_value_count_recur(current.right, target, targetCount)

    if current.left is not None:
        targetCount = tree_value_count_recur(current.left, target, targetCount)

    return targetCount


# Driver Code
a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

# print(tree_value_count(a,  6)) # -> 3

print(tree_value_count_recur(a,  6, 0)) # -> 3
