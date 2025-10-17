# Problem: Given an array of integers arr that contains n+1 elements between 1 and n inclusive,
# create a function that returns the duplicate element (the element that appears more than once). Assume that: -
# There is only one duplicate number - The duplicate number can be repeated more than once

# Naive Solution:
# We use two nested loops.
# For each element arr[i], we compare it with every element after it (arr[j]).
# As soon as we find a match, we return that number.

def findDuplicate(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return arr[i]

print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3


# Refined Solution:
# 1. Create an empty set seen to store numbers we’ve encountered.
# 2. Loop through each number in the array:
# 3. If it’s already in the set → that’s the duplicate → return it.
# 4. Otherwise, add it to the set.

def findDuplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3


# Optimal Solution:
# Use two pointers
# Idea: Treat the array as a linked list where the value at each index points to the next index.
# Cycle: Since one number repeats, it creates a loop (cycle) in this list.
# Step 1: Use two pointers (slow, fast) moving at different speeds to find where they meet inside the cycle.
# Step 2: Reset one pointer to start and move both one step at a time — they’ll meet at the duplicate number.

def findDuplicate(arr):
    # Phase 1: Find intersection point of two runners
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to the cycle (duplicate number)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3