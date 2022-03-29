# Monotonic Array

# Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

# Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase.  Similarly, non-decreasing elements aren't necessarily
# exclusively increasing; they simply don't decrease.

# Note that empty arrays and arrays of one element are monotonic.

# General Strategy
# 1. Iterate through array
#    a. compare current item to next item, note direction, if direction change, then break and return false

def isMonotonic(array):
    generalDirection = 0  # 0 is unchanged, 1 is up, -1 is down
    currentDirection = 0

    # Empty arrays and single item arrays are monotonic
    if len(array) < 2:
        return True

    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            # ascending
            currentDirection = 1
        elif array[i] > array[i+1]:
            # descending
            currentDirection = -1
        elif array[i] == array[i+1]:
            currentDirection = 0

        if generalDirection == 0:
            generalDirection = currentDirection
        elif generalDirection != currentDirection and currentDirection != 0:
            return False

    return True




# Driver Code
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

print(isMonotonic(array))
