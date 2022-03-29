# BST Traversal

# Write three functions that take in a BST and an empty array, traverse the BST and add its node
# values to the array and return the array

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree, array):
    # In Order = Left, Root, Right
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    # Pre Order = Root, Left, Right
    if tree:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    # Post Order = Left, Right, Root
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


# Driver Code
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.right = BST(22)

array = []
print("In Order Traversal", inOrderTraverse(root, array))

array = []
print("Pre Order Traversal", preOrderTraverse(root, array))

array = []
print("Post Order Traversal", postOrderTraverse(root, array))
