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

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid_idx = len(nums) // 2
    left_sorted = merge_sort(nums[:mid_idx])
    right_sorted = merge_sort(nums[mid_idx:])
    return merge(left_sorted, right_sorted)

def merge(arr1, arr2):
    sorted_arr = []
    i, j = 0,0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i +=1
        else:
            sorted_arr.append(arr2[j])
            j +=1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    return sorted_arr


numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
print(merge_sort(numbers))