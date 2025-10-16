# Given an array of integers arr, create a function that returns an array containing the values of arr
# without duplicates (the order doesn't matter).

# Solution:


def removeDuplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


print(removeDuplicates([1,1,2]))
