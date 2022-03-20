# Problem:
#
# Write a function, max_path_sum, that takes in the root of a binary tree that contains number values.
# The function should return the maximum sum of any root to leaf path within the tree.
#
# You may assume that the input tree is non-empty.

# Solution:
# 1. Traverse tree DFS or BFS
# 2. Track a running sum, sum will reset when there is a leaf node
# 3. Track maxSum


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def max_path_sum(root):
#     sum = 0
#     maxSum = 0
#     stack = []
#
#     if root is None:
#         return maxSum
#
#     stack.append(root)
#
#     while stack:
#         current = stack.pop()
#
#         if current.left is None and current.right is None:
#             if maxSum == 0:
#                 maxSum = sum
#             else:
#                 maxSum = max(sum, maxSum)
#             sum -= current.val
#         else:
#             sum += current.val
#
#         if current.right is not None:
#             stack.append(current.right)
#
#         if current.left is not None:
#             stack.append(current.left)
#
#
#     return maxSum




def max_path_sum(root):
  if root is None:
    return 0

  if root.left is None and root.right is None:
    return root.val

  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


# Driver Code
# a = Node(5)
# b = Node(11)
# c = Node(54)
# d = Node(20)
# e = Node(15)
# f = Node(1)
# g = Node(3)
#
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

# print(max_path_sum(a)) # -> 18


a = Node(5)
b = Node(10)
c = Node(20)
d = Node(8)
e = Node(10)
f = Node(3)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

print(max_path_sum(a)) # -> 30
