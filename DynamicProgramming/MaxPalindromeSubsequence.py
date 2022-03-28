# Problem:
#
# Write a function, max_palin_subsequence, that takes in a string as an argument.
# The function should return the length of the longest subsequence of the string that is also a palindrome.
#
# A subsequence of a string can be created by deleting any characters of the string,
# while maintaining the relative order of characters.

# Solution:
# Subsequence is removing any char from string while keeping the original order
# Check to see if the subsequence is a palindrome.
# Single letters or empty are palindromes
#
# 1. Loop through chars in string
# 2. For each iteration, match 1st and last chars
#    a. if match, add 2 points, remove 1st and last chars, by moving indices
#    b. if no match, recurse one with 1st remove and the other with last removed.
# 3. Sum up the points and take the larger of the two when there are multiple

def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, start, end, memo):

    key = (start, end)
    if key in memo:
        return memo[key]

    # base cases
    # length of 1
    if start == end:
        return 1

    # empty string
    if start > end:
        return 0

    if string[start] == string[end]:
        # add 2 because stripping two chars
        memo[key] = 2 + _max_palin_subsequence(string, start+1, end-1, memo)
    else:
        memo[key] = max(_max_palin_subsequence(string, start + 1, end, memo), _max_palin_subsequence(string, start, end - 1, memo))

    return memo[key]


print(max_palin_subsequence("luwxult")) # -> 5