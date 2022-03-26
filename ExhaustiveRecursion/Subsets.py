# Problem:
#
# Write a function, subsets, that takes in a list as an argument. The function should return a 2D list
# where each sublist represents one of the possible subsets of the list.
#
# The elements within the subsets and the subsets themselves may be returned in any order.
#
# You may assume that the input list contains unique elements.

# Solution:
# Given n items, there should be 2^n not combinations
#
# General approach:
# 1. visual decisions as binary tree (kinda)
# 2. at each step take nothing or take something
# 3. base case is []


def subsets(elements):
    if not elements:
        return [[]]

    first = elements[0]
    remaining_elements = elements[1:]
    subsets_without_first = subsets(remaining_elements)

    subsets_with_first = []
    # Iterate through subsets without first and add the first to each items
    for sub in subsets_without_first:
        subsets_with_first.append([first, *sub])

    # concatenate subsets_with_first and subsets_without_first
    return subsets_without_first + subsets_with_first


print(subsets(['a', 'b', 'c'])) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]