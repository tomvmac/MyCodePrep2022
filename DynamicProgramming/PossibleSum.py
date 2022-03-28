# Problem:
#
# Write a function sum_possible that takes in an amount and a list of positive numbers.
# The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list.
# You may reuse numbers of the list as many times as necessary.
#
# You may assume that the target amount is non-negative.


# Solution:
# 1. The approach is to take the target as root, subtract each number from the root, keep doing that until a 0 is reached, generating a true
# 2. Given a parent, if any of its children return true, then it is true
# 3. We can incorporate memoization to save unnecessary calculations
#
# n = length of nums
# a = amount or target
#
# Time: O(n^a) for brute, O(a * n) for memoization


def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})


def _sum_possible(amount, numbers, memo):
    if amount in memo:
        return memo[amount]

    if amount < 0:
        return False

    if amount == 0:
        return True

    for num in numbers:
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return False


print(sum_possible(8, [5, 12, 4])) # -> True, 4 + 4