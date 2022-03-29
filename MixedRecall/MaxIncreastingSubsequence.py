# Problem:
#
# Write a function, max_increasing_subseq, that takes in a list of numbers as an argument.
# The function should return the length of the longest subsequence of strictly increasing numbers.
#
# A subsequence of a list can be created by deleting any items of the list, while maintaining the relative order of items.


# Solution:
# 1. Use decision tree
# 2. On each node, decide whether to take or not to take the current node
#     a. Take current - Add 1 to calculation, pass current as previous value and increment index
#     b. Not take current - pass previous along and increment index

def max_increasing_subseq(numbers):
    return _max_increasing_subseq(numbers, 0, float('-inf'), {})


def _max_increasing_subseq(numbers, i, previous, memo):
    key = (i, previous)

    if key in memo:
        return memo[key]

    if i == len(numbers):
        return 0

    current = numbers[i]
    # options = []
    # Not take current - pass previous along and increment index
    dont_take_current = _max_increasing_subseq(numbers, i + 1, previous, memo)
    take_current = float('-inf')

    # guard against taking number if current is less than previous, because that will not be Strictly increasing
    if current > previous:
        # Take current - Add 1 to calculation, pass current as previous value and increment index
        take_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo)

    memo[key] = max(take_current, dont_take_current)
    return memo[key]


numbers = [4, 18, 20, 10, 12, 15, 19]
print(max_increasing_subseq(numbers)) # -> 5