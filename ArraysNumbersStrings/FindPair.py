# Problem:
#
# Write a function, pair_sum, that takes in an array and a target sum as arguments.
# The function should return a boolean representing whether the array contains numbers that add up to the value of k.
#
# def findPair(arr, k)


# Solution:

# Brute Force Solution:
# 2 For Loops, i, j - iterate through all possibilities and return True/False
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Refined Solution:
# Sort array
# 2 Pointers, 1 at the beginning and 1 at the end of the array.  Increment the left pointer if sum(left value + right value) is < k,
# decrement the right pointer if the sum(left value + right value) is > k.


def findPair(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == k:
            return True
        if arr[left] + arr[right] < k:
            left += 1
        if arr[left] + arr[right] > k:
            right -=1
    return False


print(findPair([1, 2, 3, 4, 5], 8))
print(findPair([1, 2, 3, 4, 5], 10))

