# Problem:
#
# Given a non-empty array of integers arr, create a function that returns the sum of the subarray
# that has the greatest sum. We don't consider the empty array [] as a subarray.

# Brute Force Solution:
# Idea:
# Consider all possible subarrays.
# For each subarray, calculate its sum.
# Keep track of the maximum sum found so far.
#
# This approach is simple but not efficient — it takes
# 𝑂(𝑛3)
# O(n3) time because:
#
# We generate all subarrays (O(n²)).
# For each subarray, we sum its elements (O(n)).

def maxSubArray(arr):
    n = len(arr)
    max_sum = arr[0]  # initialize with the first element (since array is non-empty)

    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i:j+1])  # sum of subarray arr[i..j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6


# Refined Solution:
# Instead of checking every possible subarray, we can keep track of the best subarray sum ending at each position.
#
# The key idea:
# As we move through the array, we decide for each element:
# Should we start a new subarray here?
# Or should we extend the previous subarray?
# If the sum before this element is negative, it won’t help our total — so we start fresh.

# Algorithm (Kadane’s Algorithm):
#
# Initialize two variables:
# max_sum → the overall maximum sum found so far
# current_sum → the sum of the current subarray being considered
# For each number in the array:
# Update current_sum as the maximum between:
# The current number itself (num)
# The current number plus the previous running sum (current_sum + num)
# Update max_sum if current_sum is larger.
# At the end, return max_sum.

def maxSubArray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        # Either start fresh from current number or extend the previous subarray
        current_sum = max(num, current_sum + num)

        # Update the global maximum if current_sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
