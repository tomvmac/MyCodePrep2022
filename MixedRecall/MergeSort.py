# Problem:
#
# Write a function, merge_sort, that takes in a list of numbers as an argument.
# The function should return a new list containing elements of the original list sorted in ascending order.
# Your function must implement the merge sort algorithm.

# Solution:
# Merge sort involves sorting and merge steps.
#
# Sort step:
# 1. Get mid point
# 2. Recurse left and right of mid
# 3. Merge left and right
#
# Merge step:
# 1. Take in two lists
# 2. Iterate using queue pop until one of the list is empty


from collections import deque


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid_idx = len(nums) // 2
    left_sorted = merge_sort(nums[:mid_idx])
    right_sorted = merge_sort(nums[mid_idx:])
    return merge(left_sorted, right_sorted)


def merge(list_1, list_2):
    list_1 = deque(list_1)
    list_2 = deque(list_2)

    merged = []
    while list_1 and list_2:
        # append in ascending order which ever is smaller
        if list_1[0] < list_2[0]:
            merged.append(list_1.popleft())
        else:
            merged.append(list_2.popleft())

    # include the items left over from the comparisons
    merged += list_1
    merged += list_2
    return merged


numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
print(merge_sort(numbers))