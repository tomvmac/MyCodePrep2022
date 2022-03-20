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


# Python3 program to find maximum sum leaf to root
# path in Binary Tree

# A tree node structure
class node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


max_sum_ref = 0
target_leaf_ref = None


# This function Sets the target_leaf_ref to refer
# the leaf node of the maximum path sum. Also,
# returns the max_sum using max_sum_ref
def getTargetLeaf(Node, curr_sum):

    global max_sum

    if (Node == None):
        return

    # Update current sum to hold sum of nodes on path
    # from root to this node
    curr_sum = curr_sum + Node.data

    # If this is a leaf node and path to this node has
    # maximum sum so far, then make this node target_leaf
    if (Node.left == None and Node.right == None):
        if (curr_sum > max_sum):
            max_sum = curr_sum

    # If this is not a leaf node, then recur down
    # to find the target_leaf
    getTargetLeaf(Node.left, curr_sum)
    getTargetLeaf(Node.right, curr_sum)


# Returns the maximum sum and prints the nodes on max
# sum path
def maxSumPath(Node):
    global max_sum

    # base case
    if (Node == None):
        return 0

    max_sum = -32676

    # find the target leaf and maximum sum
    getTargetLeaf(Node, 0)

    return max_sum  # return maximum sum


# Utility function to create a new Binary Tree node
def newNode(data):
    temp = node();
    temp.data = data;
    temp.left = None;
    temp.right = None;
    return temp;


# Driver function to test above functions

root = None;

# Constructing tree given in the above figure
root = newNode(5);
root.left = newNode(10);
root.right = newNode(20);
root.left.left = newNode(8);
root.left.left.left = newNode(3);
root.left.left.right = newNode(7);
root.left.right = newNode(10);

print("Following are the nodes on the maximum sum path ");
sum = maxSumPath(root);
print("\nSum of the nodes is ", sum);

# This code is contributed by Arnab Kundu

