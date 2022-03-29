# Problem:
#
# Write a function, five_sort, that takes in a list of numbers as an argument.
# The function should rearrange elements of the list such that all 5s appear at the end.
# Your function should perform this operation in-place by mutating the original list.
# The function should return the list.
#
# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.


# Solution:
#
# 1. Use two pointers, left and right, init left to beginning of list, right to be end of list
# 2. Decrement right when number is 5
# 3. Increment left when number is not 5, else swap
# 4. Loop until left crosses right


def five_sort(numbers):
    left = 0
    right = len(numbers) - 1
    temp = 0

    while left < right:
        if numbers[right] == 5:
            right -= 1

        if numbers[left] == 5:
            # swap
            temp = numbers[left]
            numbers[left] = numbers[right]
            numbers[right] = temp
        else:
            left += 1

    return numbers


# Driver Code

print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))
# -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]

print(five_sort([5, 5, 5, 1, 1, 1, 4]))
# -> [4, 1, 1, 1, 5, 5, 5]

print(five_sort([5, 5, 6, 5, 5, 5, 5]))
# -> [6, 5, 5, 5, 5, 5, 5]