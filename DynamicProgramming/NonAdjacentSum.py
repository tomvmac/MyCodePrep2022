# Problem:
#
# Write a function, non_adjacent_sum, that takes in a list of numbers as an argument.
# The function should return the maximum sum of non-adjacent items in the list.
# There is no limit on how many items can be taken into the sum as long as they are not adjacent.


# Solution:
# 1. Conceptualize as decision tree
# 2. Base case is [] -> 0
# 3. Given a current item, do one of the following:
#    a. Take the first element as edge, skip adjacent item and take the rest
#    b. Take 0 as edge, take the rest of the items


def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})


def _non_adjacent_sum(nums, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(nums):
        return 0

    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    exclude = _non_adjacent_sum(nums, i + 1, memo)
    memo[i] = max(include, exclude)
    return memo[i]