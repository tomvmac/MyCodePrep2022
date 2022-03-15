# Problem:
#
# Write a function, pair_sum, that takes in a list and a target sum as arguments.
# The function should return a tuple containing a pair of indices whose elements sum to the given target.
# The indices returned must be unique.
#
# Be sure to return the indices, not the elements themselves.
#
# There is guaranteed to be one such pair that sums to the target.


# Solution:

# 1. Iterate through list
# 2. Check to see if complement of number is in Hashmap, if not add the value as key and index position
# as value to the map.
#   3. If complement is in map, then get the position of the complement and current index


def pair_sum(numbers, target_sum):
    visitedNumbers = {}
    index = 0

    for num in numbers:
        complement = target_sum - num
        if complement not in visitedNumbers:
            visitedNumbers[num] = index
            index += 1
        else:
            return (visitedNumbers[complement], index)




# Driver Code
print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)
print(pair_sum([4, 7, 9, 2, 5, 1], 5)) # -> (0, 5)

