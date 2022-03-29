# BST Construction

# Write a BST class for a Binary Search Tree.  The class should support:
# - Inserting values with the insert method
# - Removing values with the remove method; this method should only remove the first instance of a given value
# - Searching for values with the contains method.

# Note that you can't remove values from a single-node tree.  In other words, calling the remove method on a single-node tree should simply not do anything

# Each BST node has an integer value, a left child node, and a right child node.  A node is said to be a valid BST node if and only if it satisfies
# the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values
# of every node to its right; and its children nodes are either valid BST nodes themselves or None.

# Time Complexity:
#  Avg Case: O(log(N))
#  Worst Case: O(N)  -> Single branch tree, you can't eliminate half of the tree because it's not balanced.

# Space Complexity:
#  Avg Case:  O(log(N)), space is frames on the call stack from the use of recursion
#  Worst Case: O(N), -> Single branch tree, you can't eliminate half of the tree because it's not balanced.
#  Space complexity will be O(1) if you use iterative solution.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Avg:  Time Complexity: O(log(n)) | Space: O(1)
    # Worst: O(n) time, | Space: O(1)
    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    # If the left node is None, simply create and assign the value to the left node.
                    curr.left = BST(value)
                    break
                else:
                    # Otherwise continue iterating left
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right

        return self

    def contains(self, value):
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True

        return False

    # General strategy:
    # 1. Find node that equals to value
    # 2. Remove
    #    a. If leaf node, set parent to point to None
    #    b. If has one child node, set parent to point to point to child of node to be deleted
    #    c. If has two children node, set parent to point to point to child of node to be deleted
    #    c1. and get right child's smallest left child and replace curr
    def remove(self, value, parent = None):
        curr = self
        while curr is not None:
            if value < curr.value:
                parent = curr
                curr = curr.left
            elif value > curr.value:
                parent = curr
                curr = curr.right
            else:
                # found node
                if curr.left is not None and curr.right is not None:
                    # Node has two children
                    # Get minvalue from right node's children
                    curr.value = curr.right.getMinValue()
                    # Remove the node that contained the min value
                    curr.right.remove(curr.value, curr)
                elif parent is None:
                    # Handle when parent is None
                    if curr.left is not None:
                        # Replace current node with left child's values
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        # Replace current node with right child's values
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        # No parent and no children
                        curr.value = None
                elif parent.left == curr:
                    # curr is left child
                    if curr.left is not None:
                        parent.left = curr.left
                    else:
                        parent.left = curr.right
                elif parent.right == curr:
                    # curr is right child
                    if curr.left is not None:
                        parent.right = curr.left
                    else:
                        parent.right = curr.right
                # break if value found
                break

        return self

    def getMinValue(self):
        curr = self
        while curr.left is not None:
            # Keep going left
            curr = curr.left
        return curr.value

    def traverse(self, curr):
        # In Order Traversal - Left, Root, Right
        if curr:
            self.traverse(curr.left)
            print(curr.value)
            self.traverse(curr.right)


# Driver Code
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

print(root.traverse(root))

# insert 12
root.insert(12)
print(root.traverse(root))

# contains 15
print(root.contains(15))
print(root.contains(99))

# remove 10
root
# print tree - In Order traversal

