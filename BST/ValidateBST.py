# Validate BST

# Write a function that takes in a potentially invalid Binary Search Tree and returns a boolean whether
# the BST is valid.

# Each BST node has an integer value, a left child node and a right child node.  A node is said to be valid
# BST node if and only if it satisfies BST property:
# 1. its value is strictly greater than the values of every node to its left;
# 2. its value is less than or equal to the values of every node to its right;
# 3. its children nodes are either valid BST nodes or None

# A BST is valid if and only if all of its nodes are valid BST nodes.

# General strategy:
# Traverse BST using in order tranversal (left, root, right)
# Check conditions, if any conditions are NOT true, return false



# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    rightIsValid = True
    if leftIsValid:
        rightIsValid = validateBstHelper(tree.right, tree.value, maxValue)

    return leftIsValid and rightIsValid

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

# root = BST(10)
# root.left = BST(5)
# root.left.left = BST(2)
# root.left.left.left = BST(1)
# root.left.right = BST(5)
# root.left.right.right = BST(11)
# root.right = BST(15)
# root.right.right = BST(22)

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(3)
root.left.right.right = BST(11)
root.right = BST(15)
root.right.right = BST(22)

print(validateBst(root))
