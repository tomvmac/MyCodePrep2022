# Problem:
#
# Write a function, create_combinations, that takes in a list and a length as arguments. The function should return a 2D list representing all of the combinations of the specifized length.
#
# The items within the combinations and the combinations themselves may be returned in any order.
#
# You may assume that the input list contains unique elements and 1 <= k <= len(items).


# Solution:

# Combinations is where order does not matter
#
# 1. Make 2 recursive calls
#    a. Remove first item, keep the length as is
#    b. Remove first item, reduce the length by one
# 2. Append first item into the first list
# 3. concat two list together


def create_combinations(items, k):
    if len(items) < k:
        return []

    if k == 0:
        return [[]]

    first = items[0]
    combos_with_first = []
    for combo in create_combinations(items[1:], k - 1):
        combos_with_first.append([first, *combo])

    combos_without_first = create_combinations(items[1:], k)

    return combos_with_first + combos_without_first


print(create_combinations(["a", "b", "c"], 2)) # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]