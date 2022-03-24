# Problem:
#
# Write a function, level_averages, that takes in the root of a binary tree that contains number values.
# The function should return a list containing the average value of each level.

# Solution:
# 1. BFS
# 2. When traversing, keep track of levels
# 3. For each level, take the average and store it

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_averages(root):
    if root is None:
        return []

    levels = []
    levelAverages = []
    queue = deque([(root, 0)])
    while queue:
        current, level_num = queue.popleft()

        if len(levels) == level_num:
            levels.append([current.val])
        else:
            levels[level_num].append(current.val)

        if current.left is not None:
            queue.append((current.left, level_num + 1))

        if current.right is not None:
            queue.append((current.right, level_num + 1))

    # Compute level averages
    sum = 0

    for level in levels:
        sum = 0
        levelAvg = 0
        for levelItem in level:
            sum += levelItem
        levelAvg = sum / len(level)
        levelAverages.append(levelAvg)

    return levelAverages

# Driver code:
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

print(level_averages(a)) # -> [ 3, 7.5, 1 ]

