# Problem:
#
# Write a function, permutations, that takes in a list an argument. The function should return a 2D list where each sublist represents one of the possible permutations of the list.
#
# The sublists may be returned in any order.
#
# You may assume that the input list contains unique items.

# Solution:
#
# 1. Given n items, there will be n! permutations, it's much bigger than 2^n
# 2. This is a combination of items where order matters
# 3. Get first item
# 4. Get remaining items
# 5. recursively process remaining items by looping through each item and appending first item
#    to all possible positions

def permutations(items):
    if not items:
        return[[]]

    first = items[0]
    remaining = items[1:]
    perms = permutations(remaining)
    result = []

    for perm in perms:
        # Have to add one as we are inserting the first item into the perms
        for i in range(len(perm) + 1):
            result.append([*perm[:i], first, *perm[i:]])

    return result


print(permutations(['a', 'b', 'c'])) # ->
# [
#   [ 'a', 'b', 'c' ],
#   [ 'b', 'a', 'c' ],
#   [ 'b', 'c', 'a' ],
#   [ 'a', 'c', 'b' ],
#   [ 'c', 'a', 'b' ],
#   [ 'c', 'b', 'a' ]
# ]