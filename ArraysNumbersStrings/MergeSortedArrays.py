# Problem:
#
# Given two sorted arrays nums1 and nums2, merge them into a new array.
#
# Example:
# nums1 = [1,3,4,6]
# nums2 = [2,3,5,8,9]
#
# merged = [1,2,3,3,4,5,6,8,9]

# Solution:
# 1. Iterate until arr1 is done
#    a. compare and append the smaller from the arrays and increment the appropriate counter
# 2. Process the remainder elements from arr2

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

    # Append the leftover elements from both arrays
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1


    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1


    return sorted_arr



nums1 = [1,3,4,6]
nums2 = [2,3,5,8,9]
print(merge(nums1, nums2))