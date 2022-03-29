# Find Closest Value in BST

# Write a function that take in Binary Search Tree (BST) and returns the closest value to that target value
# contained in the BST.

# You can assume that there will only be one closest value

# Each BST node has an integer value, a left child node, and a rigth child node.  A node is said to be a valid
# BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every
# node to its left, and its value is less than or equal to the values of every node to its right; and its
# children nodes are either valid BST nodes themselves or None/ null.


# This is the class of the input tree. Do not edit.
# Suck Bro method
# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, tree.value, 1000000)
#
# def findClosestValueInBstHelper(tree, target, closest, smallestDiff):
#     # General Strategy recursively go through the BST
#     # Subtract the curr value - target and take absolute value and store it as closestValue
#     # If the difference is < closestValue, replace closestValue with diff
#
#
#     if tree:
#         if target == tree.value:
#             return tree.value
#         else:
#             # calculate the closest
#             if tree.value != target:
#                 diff = abs(tree.value - target)
#                 if diff < smallestDiff:
#                     smallestDiff = diff
#                     closest = tree.value
#             if target < tree.value:
#                 return findClosestValueInBstHelper(tree.left, target, closest, smallestDiff)
#             else:
#                 return findClosestValueInBstHelper(tree.right, target, closest, smallestDiff)
#     return closest


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    # General Strategy recursively go through the BST
    # Subtract the curr value - target and take absolute value and store it as closestValue
    # If the difference is < closestValue, replace closestValue with diff


    if tree:
        if target == tree.value:
            return tree.value
        else:
            # calculate the closest
            if tree.value != target:
                if abs(tree.value - target) < abs(closest - target):
                    closest = tree.value
            if target < tree.value:
                return findClosestValueInBstHelper(tree.left, target, closest)
            else:
                return findClosestValueInBstHelper(tree.right, target, closest)
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Driver Code
# root = BST(10)
# root.left = BST(5)
# root.left.left = BST(2)
# root.left.left.left = BST(1)
# root.left.right = BST(5)
# root.right = BST(15)
# root.right.left = BST(13)
# root.right.left.right = BST(14)
# root.right.right = BST(22)
# expected = 13
# actual = findClosestValueInBst(root, 12)
#
# print("expected: ", expected)
# print("actual: ", actual)


root = BST(100)
root.left = BST(5)
root.right = BST(502)
root.right.left = BST(204)
root.right.right = BST(55000)
root.right.right.left = BST(1001)
root.right.right.right = BST(None)
root.right.right.left.left = BST(None)
root.right.right.left.right = BST(4500)


expected = 55000
actual = findClosestValueInBst(root, 30000)

print("expected: ", expected)
print("actual: ", actual)
