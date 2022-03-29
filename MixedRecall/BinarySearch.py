# Problem:
#
# Write a function, binary_search, that takes in a sorted list of numbers and a target.
# The function should return the index where the target can be found within the list.
# If the target is not found in the list, then return -1.
#
# You may assume that the input array contains unique numbers sorted in increasing order.
#
# Your function must implement the binary search algorithm.

# Solution:

def binary_search_iterative(numbers, target):
  lo = 0
  hi = len(numbers) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if target < numbers[mid]:
      hi = mid - 1
    elif target > numbers[mid]:
      lo = mid + 1
    else:
      return mid
  return -1


def binary_search_recur(arr, low, high, target):
    # base case
    if low > high:
        return -1

    # Check base case
    mid = (high + low) // 2

    # If element is present at the middle itself
    if arr[mid] == target:
        return mid

    # If element is smaller than mid, then it can only
    # be present in left subarray
    if arr[mid] > target:
        return binary_search_recur(arr, low, mid - 1, target)
    # Else the element can only be present in right subarray
    else:
        return binary_search_recur(arr, mid + 1, high, target)


# Driver code

arr = [0, 6, 8, 12, 16, 19, 20, 28]
target = 8


print(binary_search_iterative(arr, target)) # -> 2
print(binary_search_recur(arr, 0, len(arr)-1, target)) # -> 2
